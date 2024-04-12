#!/usr/bin/python3
"""A simple Flask application"""
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return a simple string 'Hello HBNB!' when accessing the root URL."""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return a simple string 'HBNB' when accessing the /hbnb URL."""
    return 'HBNB'

def c_is_fun(text):
    """Return a string 'C is fun!'"""
    return 'C' + text.replace('_', ' ')

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """Display 'Python ' followed by the text or the default 'is cool', replace underscores with spaces."""
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display 'n is a number' only if n is an integer."""
    return f'{n} is a number'

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display an HTML page only if n is an integer."""
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    # The application will listen on all public IPs (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port='5000')
