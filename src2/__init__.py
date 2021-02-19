from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from src2.controller import userBlueprint


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:123456@localhost:3306/anying_dev"
    db.init_app(app)
    app.register_blueprint(userBlueprint)
    return app
