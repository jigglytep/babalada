import yfinance as yf
from flask import request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .helper import token_required, generateJWT
from flask import Blueprint,  jsonify
from .models import User

api = Blueprint('api', __name__)


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

    # debug
    # auth = {
    #     'email': a@a.com
    #     'password': 123
    # }

    # auth = {
    #     'email': json_str.split('\n')[3].strip(),
    #     'password': json_str.split('\n')[7].strip()
    # }
    if not auth:
        # returns 
        return make_response(jsonify(
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
