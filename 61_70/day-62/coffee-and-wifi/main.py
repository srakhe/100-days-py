import pandas
from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TimeField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    location = StringField('Location URL', validators=[DataRequired()])
    open_time = TimeField('Open Time', validators=[DataRequired()])
    close_time = TimeField('Close Time', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=['☕' * i for i in range(0, 6)])
    wifi_rating_choices = ['💪' * i for i in range(1, 6)]
    wifi_rating_choices.insert(0, '✘')
    wifi_rating = SelectField('Coffee Rating', choices=wifi_rating_choices)
    power_rating = SelectField('Coffee Rating', choices=['🔌' * i for i in range(0, 6)])
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    if request.method == 'POST' and form.validate_on_submit():
        data = form.data
        with open('cafe-data.csv', 'a') as csv_file:
            csv_file.write(
                f'\n{data["cafe"]},{data["location"]},{data["open_time"]},{data["close_time"]},{data["coffee_rating"]},{data["wifi_rating"]},{data["power_rating"]}')
        return redirect(location='/')
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
