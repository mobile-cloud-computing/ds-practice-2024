from .grpc_client import greet
from flask import request

def init_routes(app):
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
