import os
from flask import Flask

from . import models
from .extentions import db, migrate
from src.routes import main, api_blueprint


def create_app():
    app = Flask(__name__)
    # database connection to flask app
    if os.getenv('SQLALCHEMY_DATABASE_URI'):
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main)
    app.register_blueprint(api_blueprint)

    return app
