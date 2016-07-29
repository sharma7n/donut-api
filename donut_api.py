# donut_api.py
# A simple API for imaginary donuts.

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_potion import Api, ModelResource


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "")
db = SQLAlchemy(app)

class Donut(db.Model):
    '''Imaginary donut model.'''
    __tablename__ = "Donut"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    maker = db.Column(db.String(64))
    flavor = db.Column(db.String(64))
    quality = db.Column(db.String(64))

    def __repr__(self):
        return 'Donut(maker={}, flavor={}, quality={})'.format(
            self.maker, self.flavor, self.quality)

class DonutResource(ModelResource):
    class Meta:
        model = Donut

api = Api(app)
api.add_resource(DonutResource)

@app.route("/")
def root():
    return "You're at the donut-api root."

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)