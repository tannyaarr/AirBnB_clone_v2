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
    """Return HBNB"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """Return C followed by the value of the <text>"""
    formatted_text = text.replace('_', ' ')
    return f'C {formatted_text}'

@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text='is cool'):
    """Displays Python followed by the value of the <text>"""
    formatted_text = text.replace('_', ' ')
    return f'Pyhton {formatted_text}'

@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """Return a number only if is an integer n"""
    return f'{n} is a number'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
