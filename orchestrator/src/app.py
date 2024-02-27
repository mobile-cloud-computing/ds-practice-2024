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

import grpc

def greet(name='you'):
    # Establish a connection with the fraud-detection gRPC service.
    with grpc.insecure_channel('fraud_detection:50051') as channel:
        # Create a stub object.
        stub = fraud_detection_grpc.HelloServiceStub(channel)
        # Call the service through the stub object.
        response = stub.SayHello(fraud_detection.HelloRequest(name=name))
    return response.greeting

def fraud(creditcard):
    with grpc.insecure_channel('fraud_detection:50051') as channel:
        stub = fraud_detection_grpc.FraudServiceStub(channel)
        response = stub.DetectFraud(fraud_detection.CheckoutRequest(creditcard=creditcard))
    return response.determination


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
    # response = greet(name='orchestrator')
    creditcard = {
        "number": "123123",
        "expirationDate": "tomorrow",
        "cvv": "123"
    }
    response = fraud(creditcard=creditcard)
    print(response)
    # Return the response.
    return str(response)

# Quick test for this: curl localhost:8081/checkout -X POST -H 'Content-Type: application/json' -H 'Referer: http://localhost:8080/' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' --data '{"user":{"name":"Priit","contact":"Asd xdc"},"creditCard":{"number":"5105105105105100","expirationDate":"12/26","cvv":"123"},"userComment":"Plz dont charge","items":[{"name":"Learning Python","quantity":1}],"discountCode":"#123","shippingMethod":"Snail","giftMessage":"","billingAddress":{"street":"Narva mnt 18u","city":"Tartu","state":"Tartumaa","zip":"51011","country":"Estonia"},"giftWrapping":false,"termsAndConditionsAccepted":true,"notificationPreferences":["email"],"device":{"type":"Smartphone","model":"Samsung Galaxy S10","os":"Android 10.0.0"},"browser":{"name":"Chrome","version":"85.0.4183.127"},"appVersion":"3.0.0","screenResolution":"1440x3040","referrer":"https://www.google.com","deviceLanguage":"en-US"}'
@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Responds with a JSON object containing the order ID, status, and suggested books.
    """

    # Print request object data
    print("Request Data:", request.json)

    # Dummy response following the provided YAML specification for the bookstore
    order_status_response = {
        'orderId': '12345',
        'status': 'Order Approved',
        'suggestedBooks': [
            {'bookId': '123', 'title': 'Dummy Book 1', 'author': 'Author 1'},
            {'bookId': '456', 'title': 'Dummy Book 2', 'author': 'Author 2'}
        ]
    }

    return order_status_response


if __name__ == '__main__':
    # Run the app in debug mode to enable hot reloading.
    # This is useful for development.
    # The default port is 5000.
    app.run(host='0.0.0.0')
