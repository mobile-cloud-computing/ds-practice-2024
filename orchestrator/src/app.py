import sys
import os
import threading

FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path_fraud_detection = os.path.abspath(os.path.join(FILE, '../../../utils/pb/fraud_detection'))
utils_path_transaction_verification = os.path.abspath(os.path.join(FILE, '../../../utils/pb/transaction_verification'))
utils_path_suggestions = os.path.abspath(os.path.join(FILE, '../../../utils/pb/suggestions'))

sys.path.insert(0, utils_path_fraud_detection)
sys.path.insert(1, utils_path_transaction_verification)
sys.path.insert(2, utils_path_suggestions)

import fraud_detection_pb2 as fraud_detection
import fraud_detection_pb2_grpc as fraud_detection_grpc

import transaction_verification_pb2 as transaction_verification
import transaction_verification_pb2_grpc as transaction_verification_grpc

import suggestions_pb2 as suggestions
import suggestions_pb2_grpc as suggestions_grpc

import grpc

def FraudDetection(request):
    with grpc.insecure_channel('fraud_detection:50051') as channel:
        stub = fraud_detection_grpc.FraudDetectionStub(channel)

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
    with grpc.insecure_channel('transaction_verification:50052') as channel:
        stub = transaction_verification_grpc.TransactionVerificationStub(channel)

        creditCard = transaction_verification.CreditCard(
            number=request['creditCard']['number'],
            expirationDate=request['creditCard']['expirationDate'],
            cvv=request['creditCard']['cvv']
            )
        response = stub.Verification(transaction_verification.VerificationRequest(creditCard=creditCard))
    return response

def SuggestionsService(request):
    with grpc.insecure_channel('suggestions:50053') as channel:
        stub = suggestions_grpc.SuggestionsServiceStub(channel)

        items = list()
        for _item in request["items"]:
            item = suggestions.Item()
            item.name = _item["name"]
            item.quantity = _item["quantity"]
            items.append(item)
        response = stub.Suggestions(suggestions.SuggestionRequest(items=items))
    return response

from flask import Flask, request
from flask_cors import CORS

# Create a simple Flask app.
app = Flask(__name__)
# Enable CORS for the app.
CORS(app)

# fraud_detection_thread = threading.Thread(target=FraudDetection)
# suggestions_thread = threading.Thread(target=SuggestionsService)
# transaction_verification_thread = threading.Thread(target=TransactionVerification)

# fraud_detection_thread.start()
# suggestions_thread.start()
# transaction_verification_thread.start()
def run_in_thread(func, args, result_dict, key):
    result_dict[key] = func(*args)

@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Responds with a JSON object containing the order ID, status, and suggested books.
    """
    print("Request Data:", request.json)

    results = {}

    fraud_detection_thread = threading.Thread(target=run_in_thread, args=(FraudDetection, (request.json,), results, 'fraud_detection'))
    suggestions_thread = threading.Thread(target=run_in_thread, args=(SuggestionsService, (request.json,), results, 'suggestions'))
    transaction_verification_thread = threading.Thread(target=run_in_thread, args=(TransactionVerification, (request.json,), results, 'transaction_verification'))

    fraud_detection_thread.start()
    suggestions_thread.start()
    transaction_verification_thread.start()

    fraud_detection_thread.join()
    suggestions_thread.join()
    transaction_verification_thread.join()

    fraud_detection_response = results['fraud_detection']
    suggestions_response = results['suggestions']
    transaction_verification_response = results['transaction_verification']

    print("Creatin response...")
    response = {
            "orderId": '123',
            "status": '',
            "suggestedBooks": []
        }

    for suggested_book in suggestions_response.suggestedBooks:
        book_dict = {
            "bookId": suggested_book.bookId,
            "title": suggested_book.title,
            "author": suggested_book.author
        }
        response["suggestedBooks"].append(book_dict)

    if fraud_detection_response.detected or not transaction_verification_response.verified:
        response['status'] = 'Order Rejected'
    else:
        response['status'] = 'Order Accepted'

    return response


if __name__ == '__main__':
    # The default port is 5000.
    app.run(host='0.0.0.0')
