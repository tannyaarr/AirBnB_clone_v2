#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)

app.route('/cities_by_states'. strict_slashes=False)
def cities_by_states():
    """Displays a web page with a list of states and citie"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda x: x.name)

    cities_data = []
    for state in states:
        cities = sorted(state.cities, key=lambda x: x.name)
        cities_data.append((state, cities))

    return render_template('cities_by_states.html', states_cities=cities_data)

@app.teardown_appcontext
def teardown_db(exception):
    """Closes the curent SQlAlchemy session"""
    storage.close()

if __name__ = '__main__':
    app.run(host='0.0.0.0'. port=5000)
