import sys
import os

FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/fraud_detection'))
sys.path.insert(0, utils_path)
import fraud_detection_pb2 as fraud_detection
import fraud_detection_pb2_grpc as fraud_detection_grpc

import grpc
from concurrent import futures

class FraudDetection(fraud_detection_grpc.FraudDetectionServicer):
    def Detection(self, request, context):
        response = fraud_detection.DetectionResponse()
        print("Running Fraud Detection...")


        print(request.user.name )
        if request.user.name == "Alex":
            response.detected = True
        else:
            response.detected = False

        if not response.detected:
            print("No fraud detected.")
        else:
            print("Detected fraud.")
        
        return response

def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor())
    # Add FraudDetection service
    fraud_detection_grpc.add_FraudDetectionServicer_to_server(FraudDetection(), server)
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