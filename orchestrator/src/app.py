import sys
import os

# This set of lines are needed to import the gRPC stubs.
# The path of the stubs is relative to the current file, or absolute inside the container.
# Change these lines only if strictly needed.
FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/fraud_detection'))
sys.path.insert(0, utils_path)
import fraud_detection_pb2 as fraud_detection
import fraud_detection_pb2_grpc as fraud_detection_grpc

# Import the transaction verification gRPC stubs
FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/transaction_verification'))
sys.path.insert(0, utils_path)
import transaction_verification_pb2 as transaction_verification
import transaction_verification_pb2_grpc as transaction_verification_grpc

import grpc

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
from flask import Flask, request, jsonify
from flask_cors import CORS

# Create a simple Flask app.
app = Flask(__name__)
# Enable CORS for the app.
CORS(app)

# Function to convert JSON data to gRPC request for transaction verification
def convert_to_verify_transaction_request(json_data):
    # Extract data from JSON and construct a TransactionRequest object
    transaction_request = transaction_verification.TransactionRequest()

    # Iterate over the JSON data and populate the fields of the TransactionRequest object
    for item_data in json_data['items']:
        item = transaction_request.items.add()
        item.item_id = item_data['item_id']
        item.name = item_data['name']
        item.quantity = item_data['quantity']
        item.price = item_data['price']

    # user_id field
    transaction_request.user_id.user_id = json_data['user_id']

    # shipping_address field
    transaction_request.shipping_address.street = json_data['shipping_address']['street']
    transaction_request.shipping_address.city = json_data['shipping_address']['city']
    transaction_request.shipping_address.state = json_data['shipping_address']['state']
    transaction_request.shipping_address.zip = json_data['shipping_address']['zip']
    transaction_request.shipping_address.country = json_data['shipping_address']['country']

    # payment_details field
    transaction_request.payment_details.number = json_data['payment_details']['number']
    transaction_request.payment_details.expiration_date = json_data['payment_details']['expiration_date']
    transaction_request.payment_details.cvv = json_data['payment_details']['cvv']
    transaction_request.payment_details.cardholder_name = json_data['payment_details']['cardholder_name']

    return transaction_request

# Function to call the transaction verification gRPC service
def verify_transaction(request):
    with grpc.insecure_channel('transaction_verification:50052') as channel:
        stub = transaction_verification_grpc.TransactionVerificationServiceStub(channel)
        response = stub.VerifyTransaction(request)
    return response

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

@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Responds with a JSON object containing the order ID, status, and suggested books.
    """
    # Print request object data
    print("Request Data:", request.json)

    verify_transaction_request = convert_to_verify_transaction_request(request.json)
    try:
        # Call the transaction verification gRPC service
        verify_transaction_response = verify_transaction(verify_transaction_request)
    except grpc.RpcError as e:
        # Handle gRPC errors, such as connection issues
        print(f"RPC failed with code {e.code()}: {e.details()}")
        return jsonify({'error': 'Failed to perform transaction verification'}), 500
    # Process verification response and handle checkout accordingly
    if verify_transaction_response.is_valid:
        # If transaction is valid, proceed with checkout process
        # Dummy response following the provided YAML specification for the bookstore
        order_status_response = {
            'orderId': '12345',
            'status': 'Order Approved',
            'suggestedBooks': [
                {'bookId': '123', 'title': 'Dummy Book 1', 'author': 'Author 1'},
                {'bookId': '456', 'title': 'Dummy Book 2', 'author': 'Author 2'}
            ]
        }
        #response_data = {'message': 'Checkout processed successfully'}
    else:
        # If transaction is invalid, handle accordingly
        #handle_invalid_transaction() # Could implement something different?
        # Dummy response for now
        order_status_response = {'error': 'Invalid transaction'}


    return order_status_response


if __name__ == '__main__':
    # Run the app in debug mode to enable hot reloading.
    # This is useful for development.
    # The default port is 5000.
    app.run(host='0.0.0.0')
