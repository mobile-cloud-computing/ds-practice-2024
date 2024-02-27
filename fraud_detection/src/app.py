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
class HelloService(fraud_detection_grpc.HelloServiceServicer):
    # Created dummy fraud detection
    def SayHello(self, request, context):

        is_fraudulent = self.check_fraud(request)
        response = fraud_detection.HelloResponse()

        if is_fraudulent:
            response.greeting = f"Fraud detected for {request.name}!"
        else:
            response.greeting = f"No fraud detected for {request.name}."

        print(response.greeting)
        
        return response
    
    def check_fraud(self, request):
        fraud_keywords = ["fraud", "scam", "fake", "illegal", "unauthorized", "guns", "terrorism"]

        for keyword in fraud_keywords:
            if keyword in request.name.lower():
                return True

def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor())
    # Add HelloService
    fraud_detection_grpc.add_HelloServiceServicer_to_server(HelloService(), server)
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