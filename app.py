import os

from flask import Flask, redirect, url_for, request, jsonify
import twilio.rest
import twilio.twiml

import config
import models


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')


@app.route("/", methods=['POST',])
def find_donut_shop():
    if request.method == 'POST':
        data = request.values
        x, y, zip_code = data['x'], data['y'], data['zip_code']
        shops = models.DonutShop.query.filter_by(zip_code=zip_code).all()
        closest_shop = min(shops, key=lambda shop: shop.distance(x, y))
        
        return jsonify({closest_shop.name: closest_shop.address})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)