from flask import Flask

app = Flask(__name__)


def make_bold(funct):
    def wrapper():
        return f'<b>{funct()}</b>'

    return wrapper


def make_italic(funct):
    def wrapper():
        return f'<em>{funct()}</em>'

    return wrapper


def make_underlined(funct):
    def wrapper():
        return f'<u>{funct()}</u>'

    return wrapper


@app.route('/')
@make_bold
@make_italic
@make_underlined
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
