import utils.pb.fraud_detection.fraud_detection_pb2 as fraud_detection
import utils.pb.fraud_detection.fraud_detection_pb2_grpc as fraud_detection_grpc

import grpc


def greet(name='you'):
    # Establish a connection with the fraud-detection gRPC service.
    with grpc.insecure_channel('fraud_detection:50051') as channel:
        # Create a stub object.
        stub = fraud_detection_grpc.HelloServiceStub(channel)
        # Call the service through the stub object.
        response = stub.SayHello(fraud_detection.HelloRequest(name=name))
    return response.greeting


def fraud(creditcard):
    with grpc.insecure_channel('fraud_detection:50051') as channel:
        stub = fraud_detection_grpc.FraudServiceStub(channel)
        response = stub.DetectFraud(fraud_detection.CheckoutRequest(creditcard=creditcard))
    return response.determination
