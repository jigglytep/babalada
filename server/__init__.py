from flask_cors import CORS
import os
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from flask import Flask
# from dotenv import load_dotenv
# load_dotenv()
# from .models import User
# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{os.environ.get("PG_USR")}:{os.environ.get("PG_PASSWD")}@{os.environ.get("PG_URL")}/postgres'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .apiPaths import api as api_blueprint
    app.register_blueprint(api_blueprint)

    return app


app = create_app()
