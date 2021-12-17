from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

API_KEY = 'tempAPIkey'


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


def give_structure(cafe, result=''):
    if cafe is None:
        if result == 'success':
            return jsonify({'success': {'Done': 'The operation was successfully completed!'}})
        elif result == 'forbidden':
            return jsonify({'error': {'Forbidden': 'Please check your API key!'}})
        else:
            return jsonify({'error': {'Not found': 'Sorry, cafe not found!'}})
    else:
        if isinstance(cafe, list):
            cafe_list = []
            for each_cafe in cafe:
                cafe_dict = {'id': each_cafe.id,
                             'name': each_cafe.name,
                             'map_url': each_cafe.map_url,
                             'img_url': each_cafe.img_url,
                             'location': each_cafe.location,
                             'seats': each_cafe.seats,
                             'has_toilet': each_cafe.has_toilet,
                             'has_wifi': each_cafe.has_wifi,
                             'has_sockets': each_cafe.has_sockets,
                             'can_take_calls': each_cafe.can_take_calls,
                             'coffee_price': each_cafe.coffee_price}
                cafe_list.append(cafe_dict)
            return jsonify(cafes=cafe_list)
        else:
            cafe_dict = {'id': cafe.id,
                         'name': cafe.name,
                         'map_url': cafe.map_url,
                         'img_url': cafe.img_url,
                         'location': cafe.location,
                         'seats': cafe.seats,
                         'has_toilet': cafe.has_toilet,
                         'has_wifi': cafe.has_wifi,
                         'has_sockets': cafe.has_sockets,
                         'can_take_calls': cafe.can_take_calls,
                         'coffee_price': cafe.coffee_price}
            return jsonify(cafe=cafe_dict)


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=['GET'])
def get_random():
    all_cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(all_cafes)
    return give_structure(random_cafe)


@app.route("/all", methods=['GET'])
def get_all():
    all_cafes = db.session.query(Cafe).all()
    return give_structure(all_cafes)


@app.route("/search", methods=['GET'])
def get_search():
    loc_arg = request.args.get('loc')
    all_cafes = db.session.query(Cafe).filter_by(location=loc_arg).first()
    return give_structure(all_cafes)


# HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def post_add_one():
    new_cafe = Cafe(name=request.form.get('name'),
                    map_url=request.form.get('map_url'),
                    img_url=request.form.get('img_url'),
                    location=request.form.get('location'),
                    seats=request.form.get('seats'),
                    has_toilet=bool(int(request.form.get('has_toilet'))),
                    has_wifi=bool(int(request.form.get('has_wifi'))),
                    has_sockets=bool(int(request.form.get('has_sockets'))),
                    can_take_calls=bool(int(request.form.get('can_take_calls'))),
                    coffee_price=request.form.get('coffee_price'))
    db.session.add(new_cafe)
    db.session.commit()
    return give_structure(None, 'success')


# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def patch_update(cafe_id):
    new_price = request.args.get('new_price')
    cafe = db.session.query(Cafe).filter_by(id=cafe_id).first()
    if cafe is None:
        return give_structure(None)
    else:
        cafe.coffee_price = new_price
        db.session.commit()
        return give_structure(None, 'success')


# HTTP DELETE - Delete Record
@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def delete_closed(cafe_id):
    apikey = request.args.get('api_key')
    if apikey == API_KEY:
        cafe = db.session.query(Cafe).filter_by(id=cafe_id).first()
        if cafe is None:
            return give_structure(None)
        else:
            db.session.delete(cafe)
            db.session.commit()
            return give_structure(None, 'success')
    else:
        return give_structure(None, 'forbidden')


if __name__ == '__main__':
    app.run(debug=True)
