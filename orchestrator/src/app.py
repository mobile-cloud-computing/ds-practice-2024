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

FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/transaction_verification'))
sys.path.insert(0, utils_path)
import transaction_verification_pb2 as transaction_verification
import transaction_verification_pb2_grpc as transaction_verification_grpc

FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/suggestions'))
sys.path.insert(0, utils_path)
import suggestions_pb2 as suggestions
import suggestions_pb2_grpc as suggestions_grpc

import grpc

def FraudDetection(request):
    # Establish a connection with the fraud-detection gRPC service.
    with grpc.insecure_channel('fraud_detection:50051') as channel:
        # Create a stub object.
        stub = fraud_detection_grpc.FraudDetectionStub(channel)
        # Call the service through the stub object.
        user = fraud_detection.User(
            name=request['user']['name'],
            contact=request['user']['contact']
            )
        billingAddress = fraud_detection.BillingAddress(
            street=request['billingAddress']['street'],
            city=request['billingAddress']['city'],
            state=request['billingAddress']['state'],
            zip=request['billingAddress']['zip'],
            country=request['billingAddress']['country'],
            )
        response = stub.Detection(fraud_detection.DetectionRequest(user=user, billingAddress=billingAddress))
    return response

def TransactionVerification(request):
    # Establish a connection with the fraud-detection gRPC service.
    with grpc.insecure_channel('transaction_verification:50052') as channel:
        # Create a stub object.
        stub = transaction_verification_grpc.TransactionVerificationStub(channel)
        # Call the service through the stub object.

        creditCard = transaction_verification.CreditCard(
            number=request['creditCard']['number'],
            expirationDate=request['creditCard']['expirationDate'],
            cvv=request['creditCard']['cvv']
            )
        response = stub.Verification(transaction_verification.VerificationRequest(creditCard=creditCard))
    return response

def SuggestionsService(request):
    # Establish a connection with the fraud-detection gRPC service.
    with grpc.insecure_channel('suggestions:50053') as channel:
        # Create a stub object.
        stub = suggestions_grpc.SuggestionsServiceStub(channel)
        # Call the service through the stub object.

        items = list()
        for _item in request["items"]:
            item = suggestions.Item()
            item.name = _item["name"]
            item.quantity = _item["quantity"]
            items.append(item)
        response = stub.Suggestions(suggestions.SuggestionRequest(items=items))
    return response

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

@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Responds with a JSON object containing the order ID, status, and suggested books.
    """
    # Print request object data
    print("Request Data:", request.json)
    response = {
            "orderId": '123',
            "status": '',
            "suggestedBooks": []
        }
    fraud_detection_response = FraudDetection(request.json)
    suggestions_response = SuggestionsService(request.json)
    transaction_verification_response = TransactionVerification(request.json)
    # suggestions_response = SuggestionsService(request.json)

    for suggested_book in suggestions_response.suggestedBooks:
        book_dict = {
            "bookId": suggested_book.bookId,
            "title": suggested_book.title,
            "author": suggested_book.author
        }
        response["suggestedBooks"].append(book_dict)

    if fraud_detection_response.detected or not transaction_verification_response.verified:
        response['status'] = 'Order Declined'
    else:
        response['status'] = 'Order Accepted'

    return response


if __name__ == '__main__':
    # Run the app in debug mode to enable hot reloading.
    # This is useful for development.
    # The default port is 5000.
    app.run(host='0.0.0.0')
