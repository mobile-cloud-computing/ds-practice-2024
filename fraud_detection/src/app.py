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
from concurrent import futures

# Create a class to define the server functions, derived from
# fraud_detection_pb2_grpc.HelloServiceServicer
class FraudDetectionService(fraud_detection_grpc.FraudDetectionServiceServicer):
    # Created dummy fraud detection
    def DetectFraud(self, request, context):
        print("Received detect fraud request")
        is_fraud = self.is_user_fraudulent(request.userName) or self.is_creditcard_fraudulent(request.creditCard)
        print(f"User {'is' if is_fraud else 'is not'} fraudulent.")
        return fraud_detection.DetectFraudResponse(isFraud=is_fraud)

    @staticmethod
    def is_user_fraudulent(username):
        blacklist = ["James"]
        return username in blacklist
    
    @staticmethod
    def is_creditcard_fraudulent(creditcard):
        return creditcard.cvv == "123"
    
def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor())
    fraud_detection_grpc.add_FraudDetectionServiceServicer_to_server(FraudDetectionService(), server)
    # Listen on port 50051
    port = "50051"
    server.add_insecure_port("[::]:" + port)
    # Start the server
    server.start()
    print(f"Server started. Listening on port {port}.")
    # Keep thread alive
    server.wait_for_termination()

if __name__ == '__main__':
    serve()