from concurrent import futures
import random
import grpc
import os
import sys

# This set of lines are needed to import the gRPC stubs.
# The path of the stubs is relative to the current file, or absolute inside the container.
# Change these lines only if strictly needed.
FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, '../../../utils/pb/suggestions'))
sys.path.insert(0, utils_path)
import suggestions_pb2 as suggestions
import suggestions_pb2_grpc as suggestions_grpc

from suggestions_pb2 import SuggestionResponse, BookSuggestion
from suggestions_pb2_grpc import SuggestionServiceServicer, add_SuggestionServiceServicer_to_server


class SuggestionService(SuggestionServiceServicer):
    all_suggestions = [
        BookSuggestion(id='1', title="The Great Gatsby", author="F. Scott Fitzgerald"),
        BookSuggestion(id='2', title="To Kill a Mockingbird", author="Harper Lee"),
        BookSuggestion(id='3', title="1984", author="George Orwell"),
        BookSuggestion(id='4', title="Pride and Prejudice", author="Jane Austen"),
        BookSuggestion(id='5', title="The Catcher in the Rye", author="J.D. Salinger"),
        BookSuggestion(id='6', title="To the Lighthouse", author="Virginia Woolf"),
        BookSuggestion(id='7', title="Moby Dick", author="Herman Melville"),
        BookSuggestion(id='8', title="The Lord of the Rings", author="J.R.R. Tolkien"),
        BookSuggestion(id='9', title="Harry Potter and the Sorcerer's Stone", author="J.K. Rowling"),
        BookSuggestion(id='10', title="The Chronicles of Narnia", author="C.S. Lewis"),
        BookSuggestion(id='11', title="The Hobbit", author="J.R.R. Tolkien"),
        BookSuggestion(id='12', title="The Da Vinci Code", author="Dan Brown"),
        BookSuggestion(id='13', title="The Alchemist", author="Paulo Coelho"),
        BookSuggestion(id='14', title="The Hunger Games", author="Suzanne Collins"),
        BookSuggestion(id='15', title="The Kite Runner", author="Khaled Hosseini"),
        BookSuggestion(id='16', title="The Fault in Our Stars", author="John Green"),
        BookSuggestion(id='17', title="The Girl with the Dragon Tattoo", author="Stieg Larsson"),
        BookSuggestion(id='18', title="The Shining", author="Stephen King"),
        BookSuggestion(id='19', title="The Catch-22", author="Joseph Heller"),
        BookSuggestion(id='20', title="The Grapes of Wrath", author="John Steinbeck"),
        BookSuggestion(id='21', title="The Picture of Dorian Gray", author="Oscar Wilde"),
        BookSuggestion(id='22', title="The Adventures of Huckleberry Finn", author="Mark Twain"),
        BookSuggestion(id='23', title="The Little Prince", author="Antoine de Saint-Exupéry"),
        BookSuggestion(id='24', title="The Scarlet Letter", author="Nathaniel Hawthorne"),
        BookSuggestion(id='25', title="The Count of Monte Cristo", author="Alexandre Dumas"),
        BookSuggestion(id='26', title="The Odyssey", author="Homer"),
        BookSuggestion(id='27', title="The Divine Comedy", author="Dante Alighieri"),
        BookSuggestion(id='28', title="The War and Peace", author="Leo Tolstoy"),
        BookSuggestion(id='29', title="The Brothers Karamazov", author="Fyodor Dostoevsky"),
        BookSuggestion(id='30', title="The Adventures of Sherlock Holmes", author="Arthur Conan Doyle"),
    ]

    def SuggestBooks(self, request, context):
        print("Received book suggestion request.")
        response = SuggestionResponse()
        response.suggestions.extend(random.choices(self.all_suggestions, k=3))
        print(f"Sending book suggestions: {', '.join([s.title for s in response.suggestions])}")
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor())
    add_SuggestionServiceServicer_to_server(SuggestionService(), server)
    port = "50053"
    server.add_insecure_port("[::]:" + port)
    server.start()
    print(f"Server started. Listening on port {port}.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()