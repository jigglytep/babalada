from flask_login import UserMixin
import datetime
from . import db
from dataclasses import dataclass


@dataclass
class User(UserMixin, db.Model):
    id: int
    email: str
    name: str
    lastname: str
    bio: str
    photoUrl: str
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    lastname = db.Column(db.String(1000))
    bio = db.Column(db.Text)
    photoUrl = db.Column(db.Text)
    # balance = db.Column(db.Integer, )


@dataclass
class Portfolio(db.Model):
    portfolioId: int
    user_id: int
    portfolioName: str
    creationDate: datetime.datetime
    balance: int
    description: str
    portfolioId = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    portfolioName = db.Column(db.String(100))
    creationDate = db.Column(db.DateTime)
    balance = db.Column(db.Integer)
    description = db.Column(db.Text)


class InvestmentTransacted(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    portfolio_id = db.Column(
        db.Integer, db.ForeignKey('portfolio.portfolioId'))
    stock_purchase = db.Column(db.String(5))
    purchase_date = db.Column(db.DateTime)
    purchase_price = db.Column(db.Integer)
    sale_date = db.Column(db.DateTime)
    sale_price = db.Column(db.Integer)
