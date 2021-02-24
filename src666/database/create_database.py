from flask_sqlalchemy import SQLAlchemy


def create_db(app):
    return SQLAlchemy(app)
