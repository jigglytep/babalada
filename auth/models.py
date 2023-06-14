from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    # balance = db.Column(db.Integer, )


# class InvestmentTransacted(db.Model):
#     id = db.Column(db.Integer)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     stock_purchase = db.Column(db.String(5))
#     purchase_date = db.Column(db.DateTime)
#     purchase_price = db.Column(db.Integer)
#     sale_date = db.Column(db.DateTime)
#     sale_price = db.Column(db.Integer)
