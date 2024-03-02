import asyncio
from concurrent import futures
import sys
import os
import uuid

# This set of lines are needed to import the gRPC stubs.
# The path of the stubs is relative to the current file, or absolute inside the container.
# Change these lines only if strictly needed.
FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
for service in ['fraud_detection', 'suggestions', 'transaction_verification']:
    sys.path.insert(0, os.path.abspath(os.path.join(FILE, f'../../../utils/pb/{service}')))

from fraud_detection_pb2_grpc import FraudDetectionServiceStub
import fraud_detection_pb2 as fraud_detection
from suggestions_pb2_grpc import SuggestionServiceStub
import suggestions_pb2 as suggestions
from transaction_verification_pb2_grpc import TransactionServiceStub
import transaction_verification_pb2 as transaction_verification

import grpc

def detect_fraud(request: fraud_detection.DetectFraudRequest) -> fraud_detection.DetectFraudResponse:
    with grpc.insecure_channel('fraud_detection:50051') as channel:
        stub = FraudDetectionServiceStub(channel)
        return stub.DetectFraud(request)
    
def verify_transaction(request: transaction_verification.VerifyRequest) -> transaction_verification.VerifyResponse:
    with grpc.insecure_channel('transaction_verification:50052') as channel:
        stub = TransactionServiceStub(channel)
        return stub.VerifyTransaction(request)
    
def get_suggestions(request: suggestions.SuggestionRequest) -> suggestions.SuggestionResponse:
    with grpc.insecure_channel('suggestions:50053') as channel:
        stub = SuggestionServiceStub(channel)
        return stub.SuggestBooks(request)

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
# Create ThreadPoolExecutor for handling gRPC requests.
executor = futures.ThreadPoolExecutor(max_workers=10)

@app.route('/checkout', methods=['POST'])
async def checkout():
    """
    Responds with a JSON object containing the order ID, status, and suggested books.
    """
    print("--- receiving new checkout request ---")

    # --- prepare requests ---
    try:
        # just using the spread operator for creating the data objects
        # is hacky and shouldl not be done in production
        transaction_verification_request = transaction_verification.VerifyRequest(
            creditCard=transaction_verification.CreditCard(**request.json['creditCard']),
            items=[transaction_verification.Item(**item) for item in request.json['items']],
        )
        fraud_detection_request = fraud_detection.DetectFraudRequest(
            userName=request.json['user']['name'],
            creditCard=fraud_detection.CreditCard(**request.json['creditCard']),
        )
        suggestion_request = suggestions.SuggestionRequest(
            bookTitles=[item['name'] for item in request.json['items']],
        )
    except (KeyError, TypeError) as e:
        print(repr(e))
        return {
            'code': "400",
            'message': "Invalid request",
        }, 400

    # --- execute requests in workers ---
    loop = asyncio.get_event_loop()
    transaction_verification_result, fraud_detection_result, suggestion_result = await asyncio.gather(
        loop.run_in_executor(executor, verify_transaction, transaction_verification_request),
        loop.run_in_executor(executor, detect_fraud, fraud_detection_request),
        loop.run_in_executor(executor, get_suggestions, suggestion_request)
    )

    order_id = str(uuid.uuid1())
    order_approved = transaction_verification_result.isValid and not fraud_detection_result.isFraud
    print(f"Order {order_id} is {'approved' if order_approved else 'rejected'}")

    # Dummy response following the provided YAML specification for the bookstore
    order_status_response = {
        'orderId': order_id,
        'status': 'Order Approved' if order_approved else 'Order Rejected',
        'suggestedBooks': [
            {
                'id': book.id,
                'title': book.title,
                'author': book.author
            }
            for book in suggestion_result.suggestions
        ]
    }

    return order_status_response


if __name__ == '__main__':
    # Run the app in debug mode to enable hot reloading.
    # This is useful for development.
    # The default port is 5000.
    app.run(host='0.0.0.0')
