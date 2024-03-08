import sys
import os

# This set of lines are needed to import the gRPC stubs.
# The path of the stubs is relative to the current file, or absolute inside the container.
# Change these lines only if strictly needed.
FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/book_suggestion'))
sys.path.insert(0, utils_path)
import book_suggestion_pb2 as book_suggestion
import book_suggestion_pb2_grpc as book_suggestion_grpc

from concurrent import futures
import grpc
import json
import random

with open(os.path.abspath(os.path.join(FILE, '../book_list.json'))) as f:
    book_list_json = json.load(f)
    book_list = [book_list_json[key] for key in book_list_json]

class BookSuggestionService(book_suggestion_grpc.BookSuggestionServiceServicer):
    def SuggestBook(self, request, context):
        print("Boook Suggestion request received")

        print(f"Ordered Book: {request.item}")
        suggest_books = random.sample(book_list, 2)
        
        return book_suggestion.BookSuggestionResponse(books=suggest_books)

    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor())
    book_suggestion_grpc.add_BookSuggestionServiceServicer_to_server(BookSuggestionService(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    print("Book Suggestion Service started on port 50053")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()