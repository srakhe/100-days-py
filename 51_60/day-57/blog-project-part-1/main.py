from flask import Flask, render_template
from datetime import datetime
import requests

copy_right = f'{datetime.today().year} Sambhav Rakhe'

app = Flask(__name__)


def get_blogs():
    response = requests.get('https://api.npoint.io/5abcca6f4e39b4955965')
    return response.json()


def get_each_blog(for_id):
    response_to_send = None
    for each_response in get_blogs():
        if each_response['id'] == for_id:
            response_to_send = each_response
    return response_to_send


@app.route('/')
def home():
    return render_template("index.html", blogs=get_blogs(), copy_right=copy_right)


@app.route('/posts/<int:blog_id>')
def blog_info(blog_id):
    return render_template("post.html", blog=get_each_blog(blog_id), copy_right=copy_right)


if __name__ == "__main__":
    app.run(debug=True)
