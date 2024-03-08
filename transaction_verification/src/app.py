import sys
import os

FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/transaction_verification'))
sys.path.insert(0, utils_path)
import transaction_verification_pb2 as transaction_verification
import transaction_verification_pb2_grpc as transaction_verification_grpc

import grpc
from concurrent import futures

class TransactionVerification(transaction_verification_grpc.TransactionVerificationServicer):
    def Verification(self, request, context):
        response = transaction_verification.VerificationResponse()
        print("Running Transaction Verification...")

        if len(request.creditCard.number)!=5:
            response.verified =  False
        else:
            response.verified = True

        if response.verified:
            print("Transaction verified successfuly..")
        else:
            print("Transaction verification failed.")

        return response

def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor())
    # Add TransactionVerification service
    transaction_verification_grpc.add_TransactionVerificationServicer_to_server(TransactionVerification(), server)
    # Listen on port 50052
    port = "50052"
    server.add_insecure_port("[::]:" + port)
    # Start the server
    server.start()
    print(f"Server started. Listening on port {port}.")
    # Keep thread alive
    server.wait_for_termination()

if __name__ == '__main__':
    serve()