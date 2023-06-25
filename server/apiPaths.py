from datetime import datetime
from flask_login import login_required
# from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint,  jsonify, request
from flask_login import login_required, current_user
from . import db
from .models import User, InvestmentTransacted
api = Blueprint('api', __name__)


@api.route('/api/')
def index():
    home = {
        "home": "welcome message",
        "status": "curent  status"
    }
    return jsonify(home)


@api.route('/api/profile')
@login_required
def api_profile():
    # user = User.query.filter_by(email=email).first()
    user = {
        "name": current_user.name,
        "email": current_user.email,
        "balance": current_user.balance
    }
    return jsonify(user)


@api.route('/api/purchase', methods=['POST'])
# @login_required
def stock_purchase():
    # user = User.query.filter_by(email=email).first()
    stock = request.form.get('stock')
    shares = request.form.get('shares')
    price = request.form.get('price')
    date = datetime.now()

    new_purchase = InvestmentTransacted(
        user_id=current_user.id,
        stock_purchase=stock,
        purchase_date=date,
        shares_purchased=shares,
        purchase_price=price)

    db.session.add(new_purchase)
    db.session.commit()

    purchase_completed = {
        "user_id": current_user.id,
        "stock_purchase": stock,
        "purchase_date": date,
        "shares_purchased": shares
    }
    return jsonify(purchase_completed)


@api.route('/api/sell', methods=['POST'])
# @login_required
def stock_sale():
    stock = request.form.get('stock')
    shares = request.form.get('shares')
    price = request.form.get('price')
    date = datetime.now()

    # id = request.form.get('id')
    # transaction = InvestmentTransacted.query.filter_by(id=id).first()
    # transaction.sale_date = date
    # db.session.commit()

    new_sale = InvestmentTransacted(
        user_id=current_user.id,
        shares_purchased=shares,
        stock_purchase=stock,
        sale_date=date,
        sale_price=price)

    db.session.add(new_sale)
    db.session.commit()
    sale_completed = {
        "user_id": current_user.id,
        "stock_sold": stock,
        "purchase_date": date,
        "shares_sold": shares
    }
    return jsonify(sale_completed)
