from flask_sqlalchemy import SQLAlchemy
from flask_potion import Api, ModelResource

from app import app


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