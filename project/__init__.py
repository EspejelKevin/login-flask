from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "development"

    db.init_app(app)

    login = LoginManager()
    login.login_view = "auth.login"
    login.init_app(app)

    from .models import User

    @login.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth
    from .main import main

    app.register_blueprint(auth)
    app.register_blueprint(main)

    return app
