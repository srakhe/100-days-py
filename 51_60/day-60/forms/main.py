from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    return f'<h2>Name: {request.form["name"]}</h2><br><h2>Password: {request.form["password"]}'


if __name__ == '__main__':
    app.run()
