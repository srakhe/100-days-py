from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)


def get_urls():
    urls: dict = {
        'css_min_url': url_for('static', filename='css/clean-blog.min.css'),
        'bootstrap_min_css_url': url_for('static', filename='vendor/bootstrap/css/bootstrap.min.css'),
        'all_min_fonts_css': url_for('static', filename='vendor/fontawesome-free/css/all.min.css'),
        'jquery_min_js_url': url_for('static', filename='vendor/jquery/jquery.min.js'),
        'bootstrap_bundle_min_url': url_for('static', filename='/vendor/bootstrap/js/bootstrap.bundle.min.js'),
        'clean_blog_min_js': url_for('static', filename='/js/clean-blog.min.js')
    }
    return urls


def get_posts():
    url = 'https://api.npoint.io/43644ec4f0013682fc0d'
    response = requests.get(url)
    return response.json()


@app.route('/')
def home():
    urls = get_urls()
    image_url = url_for('static', filename='img/home-bg.jpg')
    urls['image_url'] = image_url
    urls['all_posts'] = get_posts()
    return render_template('index.html', **urls)


@app.route('/about')
def about():
    urls = get_urls()
    image_url = url_for('static', filename='img/about-bg.jpg')
    urls['image_url'] = image_url
    return render_template('about.html', **urls)


@app.route('/contact')
def contact():
    urls = get_urls()
    image_url = url_for('static', filename='img/contact-bg.jpg')
    urls['image_url'] = image_url
    return render_template('contact.html', **urls)


@app.route('/posts/<int:num>')
def posts(num):
    urls = get_urls()
    image_url = url_for('static', filename='img/post-bg.jpg')
    urls['image_url'] = image_url
    urls['post'] = get_posts()[num-1]
    return render_template('post.html', **urls)


if __name__ == '__main__':
    app.run(debug=True)
