from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db,Restaurant,RestaurantPizza,Pizza


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

#GET /restaurants

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    restaurants_data = [
        {
            'id': restaurants.id,
            'name': restaurants.name,
            'address': restaurants.address
        }
        for restaurant in restaurants
    ]
    return jsonify(restaurants_data)