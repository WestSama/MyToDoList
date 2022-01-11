from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    
    # Config flask app
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "mysuperhypermegasecretkey"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)

    # Register blueprints
    from .view import view
    from .auth import auth

    app.register_blueprint(view, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    # Calls the function to create database
    from .dbmodel import User, Notes, Archive

    create_database(app)

    # Login manager
    login_manager = LoginManager()
    login_manager.login_view = "login.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

# Function to create database
def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)

