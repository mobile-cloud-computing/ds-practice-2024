from concurrent import futures
import grpc

from utils.pb.transaction_verification import \
    transaction_verification_pb2 as transaction_verification, \
    transaction_verification_pb2_grpc as transaction_verification_grpc

class TransactionService(transaction_verification_grpc.TransactionServiceServicer):
    def VerifyTransaction(self, request, context):
        print("Received transaction verification request.")
        response = transaction_verification.TransactionResponse()
        response.verified = self.is_request_valid(request)
        print(f"Transaction is {'valid' if response.verified else 'invalid'}.")
        return response
    
    def is_request_valid(self, request):
        # check credit card number
        if not 8 <= len(request.creditCard.number.replace(" ", "")) <= 19:
            return False
        
        # check credit card expiration date
        try:
            month, year = request.creditCard.expirationDate.split("/")
            if not 1 <= int(month) <= 12:
                return False
            if not 0 <= int(year) <= 99:
                return False
        except ValueError:
            return False
        
        # check credit card cvv
        if len(request.creditCard.cvv) != 3:
            return False
        
        # check that there is at least one item
        if len(request.items) == 0:
            return False
        
        # check that each item has a name and a quantity
        for item in request.items:
            if item.name == "":
                return False
            if item.quantity <= 0:
                return False
        
        # all checks passed, request is valid
        return True

def serve():
    server = grpc.server(futures.ThreadPoolExecutor())
    transaction_verification_grpc.add_TransactionServiceServicer_to_server(TransactionService(), server)
    port = "50052"
    server.add_insecure_port("[::]:" + port)
    server.start()
    print(f"Server started. Listening on port {port}.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()