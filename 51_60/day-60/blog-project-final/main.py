from flask import Flask, render_template, url_for, request
import requests
import configparser
import smtplib

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


@app.route('/contact', methods=['GET'])
def contact():
    urls = get_urls()
    image_url = url_for('static', filename='img/contact-bg.jpg')
    urls['image_url'] = image_url
    urls['header_message'] = 'Contact Me'
    return render_template('contact.html', **urls)


@app.route('/posts/<int:num>')
def posts(num):
    urls = get_urls()
    image_url = url_for('static', filename='img/post-bg.jpg')
    urls['image_url'] = image_url
    urls['post'] = get_posts()[num - 1]
    return render_template('post.html', **urls)


@app.route('/contact', methods=['POST'])
def form_submitted():
    urls = get_urls()
    image_url = url_for('static', filename='img/contact-bg.jpg')
    urls['image_url'] = image_url
    urls['header_message'] = 'Form Submitted Successfully'
    email = f'Name:{request.form["name"]}\nEmail:{request.form["email"]}\nPhone Number:{request.form["phno"]}\nMessage:{request.form["msg"]}'
    send_email(email_to_send=email)
    return render_template('contact.html', **urls)


def send_email(message_from_config=False, email_to_send='', receiver_email=''):
    """
    Function:
    Send an email
    Params:
    message_from_config: Bool
        Read data from config file if True
    email_to_send: str
        Data to send as email (Prefix with 'Subject:')
    """
    # Read data from config file
    config = configparser.ConfigParser()
    config.read('data/config.ini')
    # Get required data
    gmail_server = config['Gmail Server Data']
    gmail_data = config['Gmail Data']
    gmail_smtp_server = gmail_server.get('smtp_address')
    gmail_server_port = gmail_server.get('smtp_port')
    sender_email = gmail_data.get('sender')
    sender_pass = gmail_data.get('sender_pass')

    if message_from_config:
        email_content_data = config['Email Content']
        email_subject = email_content_data.get('subject')
        email_content = email_content_data.get('content')
        email_to_send = 'Subject: ' + str(email_subject) + '\n\n' + str(email_content)
        receiver_email = gmail_data.get('receiver')

    with smtplib.SMTP(str(gmail_smtp_server), int(gmail_server_port)) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_pass)
        connection.sendmail(from_addr=sender_email,
                            to_addrs=receiver_email,
                            msg=email_to_send)
    print('Email has been sent!')


if __name__ == '__main__':
    app.run(debug=True)
