import sys
from pathlib import Path

current_dir = Path(__file__).parent.absolute()
app_dir = current_dir.parent.parent
sys.path.insert(0, str(app_dir))

import utils.pb.transaction_verification.transaction_verification_pb2 as transaction_verification
import utils.pb.transaction_verification.transaction_verification_pb2_grpc as transaction_verification_grpc

import grpc
from concurrent import futures

class TransactionVerification(transaction_verification_grpc.TransactionServiceServicer):
    # Extremely transaction verification is handled here.
    def verifyTransaction(self, request, context):
        response = transaction_verification.Determination()
        response.determination = True

        # Check if credit card number is correct length.
        if not 20 > len(str(request.creditcard.number)) > 15:
            print("Invalid credit card number")
            response.determination = False

        # Check if expiration date is valid and in the future.
        try:
            import datetime
            datetime.datetime.strptime(request.creditcard.expirationDate, "%M/%y")
        except ValueError:
            print("Invalid credit card expiration date")
            response.determination = False

        # Check if CVV is valid.
        if not 1000 > int(request.creditcard.cvv) > 0 or len(str(request.creditcard.cvv)) != 3:
            print("Invalid credit card CVV")
            response.determination = False

        return response

def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor())

    transaction_verification_grpc.add_TransactionServiceServicer_to_server(TransactionVerification(), server)

    port = "50052"
    server.add_insecure_port("[::]:" + port)
    # Start the server
    server.start()
    print("Server started. Listening on port 50052.")
    # Keep thread alive
    server.wait_for_termination()


if __name__ == '__main__':
    serve()