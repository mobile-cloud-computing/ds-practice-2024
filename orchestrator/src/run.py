import sys
import os

# This set of lines is needed due to reloadium behaving differently with Python module paths than Python itself.
FILE = __file__ if '__file__' in globals() else os.getenv("PYTHONFILE", "")
utils_path = os.path.abspath(os.path.join(FILE, 'orchestrator/src/'))
sys.path.insert(0, utils_path)

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')