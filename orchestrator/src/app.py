import sys
import os

# This set of lines are needed to import the gRPC stubs.
# The path of the stubs is relative to the current file, or absolute inside the container.
# Change these lines only if strictly needed.
FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb'))
# utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/transaction_verification'))
sys.path.insert(0, utils_path)
from fraud_detection import fraud_detection_pb2 as fraud_detection
from fraud_detection import fraud_detection_pb2_grpc as fraud_detection_grpc
from transaction_verification import transaction_verification_pb2 as transaction_verification
from transaction_verification import transaction_verification_pb2_grpc as transaction_verification_grpc
from book_suggestion import book_suggestion_pb2 as book_suggestion
from book_suggestion import book_suggestion_pb2_grpc as book_suggestion_grpc

import grpc
from concurrent import futures

def greet(name='you'):
    # Establish a connection with the fraud-detection gRPC service.
    with grpc.insecure_channel('fraud_detection:50051') as channel:
        # Create a stub object.
        stub = fraud_detection_grpc.HelloServiceStub(channel)
        # Call the service through the stub object.
        response = stub.SayHello(fraud_detection.HelloRequest(name=name))
    return response.greeting

# Import Flask.
# Flask is a web framework for Python.
# It allows you to build a web application quickly.
# For more information, see https://flask.palletsprojects.com/en/latest/
from flask import Flask, request
from flask_cors import CORS

# Create a simple Flask app.
app = Flask(__name__)
# Enable CORS for the app.
CORS(app)

# Define a GET endpoint.
@app.route('/', methods=['GET'])
def index():
    """
    Responds with 'Hello, [name]' when a GET request is made to '/' endpoint.
    """
    # Test the fraud-detection gRPC service.
    response = greet(name='orchestrator')
    # Return the response.
    return response

def fraud_detection_service(data):
    with grpc.insecure_channel('fraud_detection:50051') as channel:
        stub = fraud_detection_grpc.FraudDetectionServiceStub(channel)
        response = stub.DetectFraud(fraud_detection.FraudDetectionRequest(user=data['user'], creditCard = data['creditCard']))
        return response.is_fraudulent

def transaction_verification_service(data):
    with grpc.insecure_channel('transaction_verification:50052') as channel:
        stub = transaction_verification_grpc.TransactionVerificationServiceStub(channel)
        response = stub.VerifyTransaction(transaction_verification.TransactionVerificationRequest(user=data['user'], creditCard = data['creditCard'], item = data['items'][0]))
        return response.is_valid

def book_suggestion_service(data):
    with grpc.insecure_channel('book_suggestion:50053') as channel:
        stub = book_suggestion_grpc.BookSuggestionServiceStub(channel)
        response = stub.SuggestBook(book_suggestion.BookSuggestionRequest(item=data['items'][0]))
        return response.books
    
def transform_suggested_book_response(suggested_books):
    book_array = []
    for book in suggested_books:
        book_dict = {}
        book_dict["bookId"] = book.id
        book_dict["title"] = book.title
        book_dict["author"] = book.author
        book_array.append(book_dict)

    return book_array # key: [bookId, title, author]

@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Responds with a JSON object containing the order ID, status, and suggested books.
    """
    # Print request object data
    print("Request Data:", request.json)

    data = request.json

    print("Checkout data recieved:", data)

    with futures.ThreadPoolExecutor() as executor:
        fraud_future = executor.submit(fraud_detection_service, data)
        transaction_future = executor.submit(transaction_verification_service, data)
        suggestion_future = executor.submit(book_suggestion_service, data)

        futures.wait([fraud_future, transaction_future, suggestion_future], return_when=futures.ALL_COMPLETED)

        if fraud_future.result():
            print("Checkout rejected for fraudulent reasons")
            order_status_response = {'orderId': '12345', "status": "Order Rejected because fraud was detected. Please provide a valid user name or contact."}
            return order_status_response
        
        if not transaction_future.result():
            print("Checkout rejected. Transaction verification failed")
            order_status_response = {'orderId': '12345', "status": "Transaction Invalid. Check your order and card details."}
            return order_status_response
        
    suggested_books = suggestion_future.result()
    
    order_status_response = {
        'orderId': '12345',
        'status': 'Order Approved',
        'suggestedBooks': transform_suggested_book_response(suggested_books)
    }

    return order_status_response


if __name__ == '__main__':
    # Run the app in debug mode to enable hot reloading.
    # This is useful for development.
    # The default port is 5000.
    app.run(host='0.0.0.0')
