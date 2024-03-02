from flask import request, jsonify
import asyncio

from .schemas.checkout import CheckoutSchema
from marshmallow import ValidationError
from .services.grpc_client import fraud, verify_transaction


def init_routes(app):
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
    async def checkout():
        """
        Responds with a JSON object containing the order ID, status, and suggested books.
        """

        schema = CheckoutSchema()

        order_status_response = {
            'orderId': '12345',
            'status': 'Order Approved',
            'suggestedBooks': [
                {'bookId': '123', 'title': 'Dummy Book 1', 'author': 'Author 1'},
                {'bookId': '456', 'title': 'Dummy Book 2', 'author': 'Author 2'}
            ]
        }

        try:
            data = schema.load(request.get_json())

        except ValidationError:
            return jsonify({"code": "400", "message": "Invalid request parameters."}), 400

        fraud_detection_task = asyncio.create_task(fraud(creditcard=data['creditCard']))
        verify_transaction_task = asyncio.create_task(verify_transaction(creditcard=data['creditCard']))
        # suggestions_task = asyncio.create_task(call_suggestions_service())

        # Await both tasks (i.e., the gRPC calls)
        fraud_result, verification_result = await asyncio.gather(fraud_detection_task, verify_transaction_task)

        result = {
            "fraud": fraud_result,
            "verification": verification_result
        }

        print(result)

        if not result['fraud']:
            return jsonify({"code": "400", "message": "Fraud detected."}), 400

        if not result['verification']:
            return jsonify({"code": "400", "message": "Transaction credentials are not valid."}), 400

        return jsonify(order_status_response), 200