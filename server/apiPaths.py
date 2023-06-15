from flask_login import login_required
# from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint,  jsonify
from flask_login import login_required, current_user

from . import db
from .models import User
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
    user = {
        "name": current_user.name,
        "email": current_user.email
    }
    return jsonify(user)
