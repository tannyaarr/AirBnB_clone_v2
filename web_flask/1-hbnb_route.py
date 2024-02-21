#!/usr/bin/python3
"""Starts a flask web application
    Run the Flask apllication on 0.0.0.0, port 5000
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Return the name HBNB"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
