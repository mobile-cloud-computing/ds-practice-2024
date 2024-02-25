# Import Flask.
# Flask is a web framework for Python.
# It allows you to build a web application quickly.
# For more information, see https://flask.palletsprojects.com/en/latest/
from flask import Flask, request
from flask_cors import CORS


def create_app():
    # Create a simple Flask app.
    app = Flask(__name__)
    # Enable CORS for the app.
    CORS(app)

    from .routes import init_routes
    init_routes(app)

    return app
