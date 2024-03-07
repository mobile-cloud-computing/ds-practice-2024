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


class BookSuggestionService(book_suggestion_grpc.BookSuggestionServiceServicer):
    def SuggestBook(self, request, context):
        print("Boook Suggestion request received")

        print(f"Ordered Book: {request.item}")
        suggest_books = [
            {
                "id": 1,
                "title": "THE NEW YORKER",
                "author": "The New Yorker",
                "description": "description",
                "copies": 5,
                "copiesAvailable": 3,
                "category": "magazine",
                "img": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Original_New_Yorker_cover.png",
                "price": 8.99
            },
            {
                "id": 2,
                "title": "ESTONIA - A MODERN HISTORY",
                "author": "NEIL TAYLOR",
                "description": "description",
                "copies": 2,
                "copiesAvailable": 3,
                "category": "history",
                "img": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1526892615i/40186083.jpg",
                "price": 23.5
            }
        ]
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