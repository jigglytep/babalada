# from models import User
from functools import wraps
from flask import jsonify, request
from datetime import datetime, timedelta
import jwt
from .models import User


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        from . import app

        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message': 'Token is missing !!'}), 401

        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(
                token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.query\
                .filter_by(id=data['id'])\
                .first()
        except:
            return jsonify({
                'message': 'Token is invalid !!'
            }), 401
        # returns the current logged in users context to the routes
        return f(current_user, *args, **kwargs)

    return decorated


def generateJWT(user):
    from . import app
    return jwt.encode({
        'id': user.id,
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }, app.config['SECRET_KEY'], algorithm="HS256")
