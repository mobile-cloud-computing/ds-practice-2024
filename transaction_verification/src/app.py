import sys
import os
import grpc
from concurrent import futures

# Import gRPC stubs
FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/transaction_verification'))
sys.path.insert(0, utils_path)
import transaction_verification_pb2 as transaction_verification
import transaction_verification_pb2_grpc as transaction_verification_grpc

# Define the transaction verification logic
def verify_transaction(transaction_data):
    # Check if the list of items is not empty
    if not transaction_data.get('items'):
        return False, "No items in the transaction"

    # Check if required user data is filled-in
    if not all(transaction_data.get(field) for field in ['user_id', 'shipping_address', 'payment_details']):
        return False, "Missing user data"

    # Check if the credit card format is correct (you can use a regex or a library for this)
    if not is_valid_credit_card(transaction_data['payment_details'].get('credit_card')):
        return False, "Invalid credit card format"
    # Implement your transaction verification logic here
    # This could include checks for non-empty items list, required user data, credit card format, etc.
    # Return a boolean indicating whether the transaction is valid, along with a message
    return True, "Transaction is valid"

def is_valid_credit_card(credit_card_number):
    # Implement credit card validation logic (e.g., using regex or a library)
    # Return True if the credit card number is valid, False otherwise
    pass

# Create a class for the TransactionVerification service
class TransactionVerificationService(transaction_verification_grpc.TransactionVerificationServiceServicer):
    def VerifyTransaction(self, request, context):
        # Extract transaction data from the gRPC request
        transaction_data = {
            'items': request.items,
            'user_id': request.user_id,
            'shipping_address': request.shipping_address,
            'payment_details': {
                'credit_card': request.credit_card
            }
        }
        # Perform transaction verification
        is_valid, message = verify_transaction(transaction_data)
        # Create a response message
        response = transaction_verification.TransactionResponse()
        response.is_valid = is_valid
        response.message = message
        return response

# Define the serve function to start the gRPC server
def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor())
    # Add the TransactionVerification service
    transaction_verification_grpc.add_TransactionVerificationServiceServicer_to_server(TransactionVerificationService(), server)
    # Listen on port 50052
    port = "50052"
    server.add_insecure_port("[::]:" + port)
    # Start the server
    server.start()
    print("Transaction Verification Server started. Listening on port 50052.")
    # Keep the thread alive
    server.wait_for_termination()

# Entry point of the script
if __name__ == '__main__':
    serve()