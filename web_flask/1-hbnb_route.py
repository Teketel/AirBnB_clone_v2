# /usr/bin/python3
'''
Flask web app serve / and /hbnb
'''

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_flask():
    """Return 'Hello HBNB!' string
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Return 'HBNB' string
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
