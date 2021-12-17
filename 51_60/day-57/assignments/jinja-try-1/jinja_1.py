from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def home():
    number = random.randint(0, 100)
    headlines = f'Sambhav Rakhe = {number}'
    return render_template('index.html', headlines=headlines)


if __name__ == '__main__':
    app.run(debug=True)
