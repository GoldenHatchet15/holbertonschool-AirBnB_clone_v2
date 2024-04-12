#!/usr/bin/python3
"""A simple Flask application"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity

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

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Display an HTML page only if n is an integer."""
    result="even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', n=n, result=result)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a HTML page with a list of all States."""
    states = storage.all("State").values()
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def close_session(exception):
    """Remove the current SQLAlchemy session."""
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page with a list of all States and their Cities."""
    states = storage.all("State").values()
    # Sort states by name and cities by name under each state
    states = sorted(states, key=lambda state: state.name)
    for state in states:
        state.cities = sorted(state.cities, key=lambda city: city.name)
    return render_template('8-cities_by_states.html', states=states)

@app.route('/states', strict_slashes=False)
def list_states():
    """Display a HTML page with a list of all States."""
    states = storage.all(State).values()
    return render_template('9-states.html', states=states, id=None)

@app.route('/states/<id>', strict_slashes=False)
def list_cities(id):
    """Display a HTML page with a list of Cities in a State."""
    states = storage.all(State).values()
    state = next((s for s in states if s.id == id), None)
    return render_template('9-states.html', states=states, id=id, state=state)

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Render the hbnb filters page."""
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    amenities = list(storage.all(Amenity).values())
    amenities.sort(key=lambda x: x.name)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
