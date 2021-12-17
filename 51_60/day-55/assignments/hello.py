from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align:center">Hello, World!<h1>' \
           '<p align="center"><img src="https://media.giphy.com/media/P8KTCQ3zUoU61TVRaZ/giphy.gif" height=300 width=300/></p>'


# Routing with url
@app.route('/bye')
def bye():
    return 'Bye!'


# Routing with variables!
@app.route('/user/<name>')
def greet(name):
    return f'Hello {name}!'


# Using converter
@app.route('/get/<string:name>/<int:num>')
def get(name, num):
    print(f'{type(name)}{type(num)}')
    return f'{name}{num}'


# Using path from url
@app.route('/path/<path:rem_path>')
def print_path(rem_path):
    return f'This is {rem_path.title()}'


if __name__ == '__main__':
    app.run(debug=True)
