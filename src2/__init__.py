import logging
import logging.handlers

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from src2.views import userBlueprint


def create_app():
    # 初始化app
    app = Flask(__name__)
    # app配置项
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:123456@localhost:3306/anying_dev"
    # 数据库初始化
    db.init_app(app)
    # 蓝图
    app.register_blueprint(userBlueprint)
    # 初始化log
    # app.logger.name = 'app'
    socketHandler = logging.handlers.SocketHandler('localhost', logging.handlers.DEFAULT_TCP_LOGGING_PORT)
    app.logger.addHandler(socketHandler)
    return app
