#!/usr/bin/python3
"""Starts a Flask web appliction"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Lists all states"""
    states = storage.all(State).values()
    sorted_stated = sorted(states, key=lambda state: state.name)

    return render_template('states_list.html', states=sorted_states)

@app.teardown_appcontext
def teardown(execption):
    """Removes the current SQLAlchem session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
