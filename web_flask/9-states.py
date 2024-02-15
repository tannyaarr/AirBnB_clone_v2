#!/usr/bin/python3
"""Starts a flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)
@app.route('/states', strict_slashes=False)
def list_state():
    """Display a web page with a liat of states"""
    states = storage.all(State).values()
    states = sorted(states. key=lambda x: x.name)
    return render_template('states.html', states=states)

@app.route('/states/<id>', strict_slashes=False)
def show_state(id):
    """Displays a web page with details of a state and its cities"""
    state = storage.get(State, id)
    if state:
        cities = sorted(state.cities, key=lambda x: x.name)
        return render_template('state.html', state=state, cities=cities)
    else:
        return render_template('not_found.html')

@app.teardown_appcontext
def teardown_db(exception):
    """Closes the current SQLAlchemy session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
