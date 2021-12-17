from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange
import requests
import os

MOVIE_DB_API_KEY = os.environ['MOVIE_DB_API_KEY']

app = Flask(__name__)
app.config['SECRET_KEY'] = '9a53fe169568036a64202921aa209a8e'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies_list.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class EditForm(FlaskForm):
    rating = FloatField('Rating:', validators=[DataRequired(), NumberRange(min=0, max=10)])
    review = StringField('Review:', validators=[DataRequired()])
    submit = SubmitField(validators=[DataRequired()])


class AddForm(FlaskForm):
    title = StringField('Title:', validators=[DataRequired()])
    submit = SubmitField('Add Movie', validators=[DataRequired()])


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=False, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.String(255), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=True)
    ranking = db.Column(db.Integer, unique=False, nullable=True)
    review = db.Column(db.String(255), unique=False, nullable=True)
    image_url = db.Column(db.String(255), unique=False, nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'


def db_setup():
    db.create_all()


db_setup()


@app.route("/")
def home():
    results = db.session.query(Movie).all()

    def get_my_key(obj):
        return obj.rating

    if not len(results) == 0:
        i = 1
        results.sort(key=get_my_key, reverse=True)
        for result in results:
            result.ranking = i
            i += 1
        db.session.commit()

    return render_template("index.html", movies_list=results)


@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    if not request.method == 'POST':
        form = EditForm()
        movie = db.session.query(Movie).filter_by(id=id).first()
        return render_template('edit.html', movie=movie, form=form)
    else:
        form = request.form
        rating = form['rating']
        review = form['review']
        movie = db.session.query(Movie).filter_by(id=id).first()
        movie.rating = rating
        movie.review = review
        db.session.commit()
        return redirect('/')


@app.route("/delete/<int:id>")
def delete(id):
    movie = db.session.query(Movie).filter_by(id=id).first()
    db.session.delete(movie)
    db.session.commit()
    return redirect('/')


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        form = AddForm()
        return render_template('add.html', form=form)
    else:
        params = {
            'api_key': MOVIE_DB_API_KEY,
            'query': request.form['title']
        }
        response = requests.get('https://api.themoviedb.org/3/search/movie', params=params)
        return render_template('select.html', results=response.json()["results"])


@app.route("/add/<int:id>")
def add_to_db(id):
    params = {
        'api_key': MOVIE_DB_API_KEY
    }
    response = requests.get(f'https://api.themoviedb.org/3/movie/{id}', params=params)
    movie_data = response.json()
    new_movie = Movie(
        title=movie_data['title'],
        year=movie_data['release_date'][0:4],
        description=movie_data['overview'],
        rating=None,
        ranking=None,
        review=None,
        image_url=f'https://image.tmdb.org/t/p/w500/{movie_data["backdrop_path"]}'
    )
    db.session.add(new_movie)
    db.session.commit()
    results = db.session.query(Movie).filter_by(title=movie_data['title']).first()
    id_to_update = results.id
    return redirect(f'/update/{id_to_update}')


if __name__ == '__main__':
    app.run(debug=True)
