import yfinance as yf
from flask import request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .helper import token_required, generateJWT
from flask import Blueprint,  jsonify
from .models import User, Portfolio, InvestmentTransacted
from datetime import datetime
api = Blueprint('api', __name__)


@api.route('/api/portfolio/new', methods=["POST"])
@token_required
def newPortfolio(current_account):
    data = request.form
    portfolio = Portfolio(
        user_id=current_account.id,
        portfolioName=data['portfolioName'],
        creationDate=datetime.now(),
        balance=data['balance'],
        description=data['description']
    )
    db.session.add(portfolio)
    db.session.commit()
    return jsonify()


@api.route('/api/stock/transaction', methods=["POST"])
@token_required
def stockTransaction(current_account):
    data = request.form

    transaction = InvestmentTransacted(
        id=data['id'],
        portfolio_id=data['portfolio_id'],
        stock_purchase=data['stock_purchase'],
        purchase_date=data['purchase_date'],
        purchase_price=data['purchase_price'],
        sale_date=data['sale_date'],
        sale_price=data['sale_price']
    )
    db.session.add(transaction)
    db.session.commit()
    return jsonify()


@api.route('/api/<portfolioID>/transactions', methods=["GET"])
def getPortfoliotransactions(portfolioID):
    portfolios = InvestmentTransacted.query(portfolio_id=portfolioID).all()
    return make_response(jsonify({'portfolios': portfolios}), 201)


@api.route('/api/portfolios', methods=["GET"])
def getPortfolios():
    portfolios = Portfolio.query.all()
    return make_response(jsonify({'portfolios': portfolios}), 201)


@api.route('/api/portfolio/change', methods=["DELETE", "POST"])
@token_required
def changePortfolio(current_account):
    data = request.form
    if request.method == 'POST':
        try:
            portfolio = Portfolio.query\
                .filter_by(portfolioId=data['portfolioId'])\
                .first()

            # user_id = current_account.id,
            portfolio.portfolioName = data.get(
                'portfolioName', portfolio.portfolioName),
            portfolio.balance = data.get('balance', portfolio.balance),
            portfolio.description = data.get(
                'description', portfolio.description)
            db.session.add(portfolio)
            db.session.commit()
            return jsonify('Portfolio updated',
                           200,
                           {f"Portfolio {data['portfolioId']}": f"updated"})
        except:
            return jsonify('Portfolio failed to updated',
                           200,
                           {f"Portfolio {data['portfolioId']}": f"Failed to updated"})

    elif request.method == 'DELETE':
        try:
            portfolio = Portfolio.query.filter_by(
                portfolioId=data['portfolioId']).delete()
            db.session.commit()
            return jsonify('Portfolio deleted',
                           200,
                           {f"Portfolio {data['portfolioId']}": f"deleted"})
        except:
            return jsonify('Portfolio failed to delete',
                           200,
                           {f"Portfolio {data['portfolioId']}": f"Failed to Delete"})


@api.route('/api/')
def index():
    home = {
        "home": "welcome message",
        "status": "curent  status"
    }
    return jsonify(home)


@api.route('/api/account')
@token_required
def api_account(current_account):
    account = {
        "name": current_account.name,
        "email": current_account.email
    }
    return jsonify(account)


@api.route('/api/login', methods=['POST'])
def login():
    # json_str = request.data.decode('utf-8')
    auth = request.form

    if not auth:
        # returns
        return (jsonify(
            'Could not verify',
            401,
            {'WWW-Authenticate': 'Basic realm ="Form required !!"'}
        ))

    if not auth.get('email') or not auth.get('password'):
        # returns 401 if any email or / and password is missing
        return make_response(jsonify(
            'Could not verify',
            401,
            {'WWW-Authenticate': 'Basic realm ="Login required !!"'}
        ))

    user = User.query\
        .filter_by(email=auth.get('email'))\
        .first()
    if not user:
        # returns 401 if user does not exist
        return make_response(jsonify(
            'Could not verify',
            401,
            {'WWW-Authenticate': 'Basic realm ="User does not exist !!"'}
        ))

    if check_password_hash(user.password, auth.get('password')):
        # generates the JWT Token
        token = generateJWT(user)

        return make_response(jsonify({'token': token}), 201)
    # returns 403 if password is wrong
    return make_response(jsonify(
        'Could not verify',
        403,
        {'WWW-Authenticate': 'Basic realm ="Wrong Password !!"'}
    ))


@api.route('/api/signup', methods=['POST'])
def signup():

    # creates a dictionary of the form data
    data = request.form

    # Debug
    # data = {
    #     'name': 'fof',
    #     'email': 'f@f.com',
    #     'password': '123'
    # }

    # gets name, email and password
    name, email = data.get('name'), data.get('email')
    password = data.get('password')

    # checking for existing user
    user = User.query\
        .filter_by(email=email)\
        .first()
    if not user:
        # database ORM object
        user = User(
            name=name,
            email=email,
            password=generate_password_hash(password, method='sha256')
        )
        # insert user
        db.session.add(user)
        db.session.commit()

        token = generateJWT(user)

        return make_response(jsonify({'token': token}), 201)
    else:
        return make_response(jsonify('User already exists. Please Log in.', 202))


@api.route('/api/stock_info/<ticker>', methods=['GET'])
def stock_info(ticker="MSFT"):
    data = yf.Ticker(ticker)
    return make_response(jsonify(data.info, 200))
