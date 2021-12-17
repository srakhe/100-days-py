from flask import Flask, render_template
import requests

app = Flask(__name__)


def get_blog_data():
    url = 'https://api.npoint.io/5abcca6f4e39b4955965'
    response = requests.get(url)
    return response.json()


@app.route('/')
def home():
    blogs = '[]'
    return render_template('index.html', blogs=blogs)


@app.route('/blogs/<something>')
def blog_page(something):
    print(something)
    blogs = get_blog_data()
    return render_template('index.html', blogs=blogs)


if __name__ == '__main__':
    app.run(debug=True)
