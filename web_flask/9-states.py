#!/usr/bin/python3
"""A simple Flask application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from os import getenv


app = Flask(__name__)
app.url_map.strict_slashes = False  # Apply strict_slashes=False globally


@app.route('/')
def hello_hbnb():
    """Return a simple string 'Hello HBNB!' when accessing the root URL."""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Return a simple string 'HBNB' when accessing the /hbnb URL."""
    return 'HBNB'


def c_is_fun(text):
    """Return a string 'C is fun!'"""
    return 'C' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """Return a string 'Python is cool!'"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n):
    """Display 'n is a number' only if n is an integer."""
    return f'{n} is a number'


@app.route('/number_template/<int:n>')
def number_template(n):
    """Display an HTML page only if n is an integer."""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Display an HTML page only if n is an integer."""
    result = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', n=n, result=result)


@app.route('/states_list')
def states_list():
    """Display an HTML page that lists all State objects in the database."""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template("7-states_list.html", states=sorted_states)


@app.route('/cities_by_states')
def cities_by_states():
    """ Display the states and cities listed in the database. """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    """If needed, sort cities of each state as well"""
    for state in states:
        state.cities = sorted(state.cities, key=lambda city: city.name)
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states')
def list_states():
    """Display a HTML page with a list of all States."""
    states = storage.all(State).values()
    return render_template('9-states.html', states=states, id=None)

@app.route('/states/<id>')
def list_cities(id):
    """Display a HTML page with a list of Cities in a State."""
    states = storage.all(State).values()
    state = next((s for s in states if s.id == id), None)
    return render_template('9-states.html', states=states, id=id, state=state)

@app.route('/states', defaults={'id': None})
@app.route('/states/<id>')
def list_states_cities(id):
    """Display a HTML page with a list of all States or cities in a State if id is provided."""
    states = storage.all(State).values()
    state = None
    if id:
        state = next((s for s in states if s.id == id), None)
    return render_template('9-states.html', states=states, id=id, state=state)



@app.teardown_appcontext
def close_session(exception):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
