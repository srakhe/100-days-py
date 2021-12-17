from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    content = 'Please enter your name in the URL!'
    copyright = f'{datetime.today().year}'
    return render_template('index.html', content=content, copyright=copyright)


def get_age(name):
    url = f'https://api.agify.io?name={name}'
    response = requests.get(url)
    print(response.json()['age'])
    return response.json()['age']


def get_gender(name):
    url = f'https://api.genderize.io?name={name}'
    response = requests.get(url)
    print(response.json()['gender'])
    return response.json()['gender']


@app.route('/<name>')
def guesser(name):
    content = f'Your gender guessed is: {get_gender(name).title()}. Your age guessed is: {get_age(name)}.'
    copyright = f'{datetime.today().year}'
    return render_template('index.html', content=content, copyright=copyright)


if __name__ == '__main__':
    app.run(debug=True)
