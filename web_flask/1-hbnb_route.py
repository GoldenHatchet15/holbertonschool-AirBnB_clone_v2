#!/usr/bin/python3
"""A simple Flask application"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return a simple string 'Hello HBNB!' when accessing the root URL."""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return a simple string 'HBNB' when accessing the /hbnb URL."""
    return 'HBNB'

if __name__ == "__main__":
    # The application will listen on all public IPs (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port='5000')
