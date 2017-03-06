import os

from flask import Flask, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_potion import Api, ModelResource
from twilio.rest import TwilioRestClient

import config


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)

class DonutShop(db.Model):
    __tablename__ = 'DonutShop'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    address = db.Column(db.String(256))
    zip_code = db.Column(db.String(128))
    x_coordinate = db.Column(db.Integer)
    y_coordinate = db.Column(db.Integer)

    def distance(self, x, y):
        return (self.x_coordinate - int(x))^2 + (self.y_coordinate - int(y))^2

db.create_all()

class DonutShopResource(ModelResource):
    class Meta:
        model = DonutShop

api = Api(app)
api.add_resource(DonutShopResource)

@app.route("/", methods=['POST',])
def find_donut_shop():
    if request.method == 'POST':
        data = request.values
        x, y, zip_code = data['x'], data['y'], data['zip_code']
        shops = DonutShop.query.filter_by(zip_code=zip_code).all()
        closest_shop = min(shops, key=lambda shop: shop.distance(x, y))
        return jsonify({closest_shop.name: closest_shop.address})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)