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
    # Create an RPC function to say hello
    def SayHello(self, request, context):
        # Create a HelloResponse object
        response = fraud_detection.HelloResponse()
        # Set the greeting field of the response object
        response.greeting = "Hello, " + request.name
        # Print the greeting message
        print(response.greeting)
        # Return the response object
        return response


class FraudService(fraud_detection_grpc.FraudServiceServicer):
    # Extremely simplistic fraud detection is handled here.
    def DetectFraud(self, request, context):
        response = fraud_detection.Determination()
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
    # Add HelloService
    fraud_detection_grpc.add_HelloServiceServicer_to_server(HelloService(), server)
    fraud_detection_grpc.add_FraudServiceServicer_to_server(FraudService(), server)
    # Listen on port 50051
    port = "50051"
    server.add_insecure_port("[::]:" + port)
    # Start the server
    server.start()
    print("Server started. Listening on port 50051.")
    # Keep thread alive
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
