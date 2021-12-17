from flask import Flask
import random

app = Flask(__name__)

number = 0
colors = ['blue', 'red', 'green', 'yellow', 'orange']


@app.route('/')
def home():
    global number
    page = '<h1 align="center">Welcome to higher/lower</h1>' \
           '<h1 align="center">Please guess a number between 0 and 9 by entering in the url!</h1>' \
           '<h1 align="center">Come back here to refresh the number to guess</h1>' \
           '<p align="center"><img src="https://media.giphy.com/media/13RcbHeXlLNysE/giphy.gif"/></p>'
    number = random.randint(0, 9)
    return page


@app.route('/<int:num>')
def guessing(num):
    global number
    color = random.choice(colors)
    if num < number:
        gif_url = 'https://media.giphy.com/media/TgmiJ4AZ3HSiIqpOj6/giphy.gif'
        message = 'Go Higher Please!'
    elif num > number:
        print('Go lower!')
        gif_url = 'https://media.giphy.com/media/l4FB8UWQN6SqpPa2A/giphy.gif'
        message = 'Go Lower Please!'
    else:
        print('Found me!')
        gif_url = 'https://media.giphy.com/media/xT0xeBEo61p5XGl9Di/giphy.gif'
        message = 'You found it!'
    return f'<h1 align="center" style="color:{color};">{message}</h1>' \
           f'<p align="center"><img src="{gif_url}"/></p>'


if __name__ == '__main__':
    app.run(debug=True)
