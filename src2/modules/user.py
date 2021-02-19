from src2 import db
from datetime import datetime

Base = db.Model


class User(db.Model):
    # __tablename__ = "users"
    # __table_args__ = {"useexisting": True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False, )  # id:主键 唯一 自增 不为空
    email = db.Column(db.String(255), unique=True, nullable=False)  # email:唯一 不为空
    password = db.Column(db.String(255), nullable=False)  # 密码:(使用md5加密) 不为空
    username = db.Column(db.String(255), unique=True, nullable=False)  # username:唯一 不为空
    hasUsername = db.Column(db.Boolean, nullable=False, default=False)  # hasUsername: 不为空 默认为否
    nickname = db.Column(db.String(255), nullable=False, default="default_nickname")  # nickname:不为空
    user_create_time = db.Column(db.DateTime, default=datetime.now())
    user_last_login_time = db.Column(db.DateTime, default=datetime.now())
    token = db.Column(db.String(255))
    user_token_create_time = db.Column(db.DateTime)

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.username = "unset_username_" + email
        self.nickname = "扶我起来, 我还能学!"
        self.token = "this a token"
        self.user_token_create_time = datetime.now()
