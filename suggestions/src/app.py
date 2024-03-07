import sys
import os

FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/suggestions'))
sys.path.insert(0, utils_path)
import suggestions_pb2 as suggestions
import suggestions_pb2_grpc as suggestions_grpc

import grpc
from concurrent import futures

class Suggestions(suggestions_grpc.SuggestionsServiceServicer):
    def Suggestions(self, request, context):
        response = suggestions.SuggestionResponse()
        print("Looking for Suggestions...")

        book = {'bookId': '123', 'title': 'Dummy Book 1', 'author': 'Author 1'}
        book = suggestions.Book()
        book.bookId = "123"
        book.title = "Dummy Book 1"
        book.author = "Author 1"
        response.suggestedBooks.append(book)
        book = suggestions.Book()
        book.bookId = "123"
        book.title = "Dummy Book 1"
        book.author = "Author 1"
        response.suggestedBooks.append(book)
        book = suggestions.Book()
        book.bookId = "123"
        book.title = "Dummy Book 1"
        book.author = "Author 1"
        response.suggestedBooks.append(book)

        return response

def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor())
    # Add Suggestions service
    suggestions_grpc.add_SuggestionsServiceServicer_to_server(Suggestions(), server)
    # Listen on port 50053
    port = "50053"
    server.add_insecure_port("[::]:" + port)
    # Start the server
    server.start()
    print(f"Server started. Listening on port {port}.")
    # Keep thread alive
    server.wait_for_termination()

if __name__ == '__main__':
    serve()