from flask import Flask, render_template, redirect, request
from myForm import MyForm
from flask_bootstrap import Bootstrap


def create_app():
    app = Flask(__name__)
    app.secret_key = "some secret string"
    Bootstrap(app)
    return app


app = create_app()


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if email.casefold() == 'admin@email.com' and password.casefold() == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
