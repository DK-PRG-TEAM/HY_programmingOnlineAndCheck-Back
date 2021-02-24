from src import db
from datetime import datetime

Base = db.Model


class User(db.Model):
    # __tablename__ = "users"
    # __table_args__ = {"useexisting": True}
    # 用户唯一ID
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True, nullable=False,
                   comment="用户ID")  # id:主键 唯一 自增 不为空
    # 用户密码
    password = db.Column(db.String(255), nullable=False, comment="用户密码")  # 密码:(使用md5加密) 不为空
    hasPassword = db.Column(db.Boolean, nullable=False, default=False, comment="是否存在用户密码")
    # 用户邮箱
    email = db.Column(db.String(255), unique=True, nullable=False, comment="用户邮箱(可用于登录)")  # email:唯一 不为空
    hasEmail = db.Column(db.Boolean, nullable=False, default=False, comment="是否存在邮箱")
    # 用户名
    username = db.Column(db.String(255), unique=True, nullable=False, comment="用户名(可用于登录)")  # username:唯一 不为空
    hasUsername = db.Column(db.Boolean, nullable=False, default=False, comment="是否存在用户名")  # hasUsername: 不为空 默认为否
    # 用户手机号
    telephone = db.Column(db.String(255), unique=True, comment="用户手机号")
    hasTelephone = db.Column(db.Boolean, default=False, comment="是否存在手机号")

    # -----用户其他信息-----
    # 安全相关
    user_last_login_ip = db.Column(db.String(255), comment="用户最后登录IP")
    # 时间相关
    user_create_time = db.Column(db.DateTime, default=datetime.now(), comment="用户创建时间")
    user_last_login_time = db.Column(db.DateTime, default=datetime.now(), comment="用户最后登陆时间")
    # token相关
    hasToken = db.Column(db.Boolean, nullable=False, default=False, comment="是否存在token")
    token = db.Column(db.String(255), comment="用户Token")
    user_token_create_time = db.Column(db.DateTime, comment="用户Token创建时间")
    # 用户资料
    nickname = db.Column(db.String(255), nullable=False, default="unset_nickname", comment="用户昵称")  # nickname:不为空
    avatar_images_url = db.Column(db.String(255), nullable=False, default="unset_avatar", comment="用户头像url")

    def __init__(self, email, password):
        self.__initBaseInfo(email)
        self.hasEmail = True
        self.hasPassword = True
        self.email = email
        self.password = password

    def __initBaseInfo(self, userCreateMethod):
        # 初始化设置邮箱注册
        self.hasEmail = False
        self.hasUsername = False
        self.hasTelephone = False
        self.hasPassword = False
        self.hasToken = False
        # 初始化未启用的字段
        self.password = "unset_password"
        self.email = "unset_email_" + userCreateMethod
        self.username = "unset_username_" + userCreateMethod
        self.telephone = "unset_telephone_" + userCreateMethod
        self.token = "unset_token"
        # 初始化用户其他信息
        self.nickname = "扶我起来, 我还能学!"
        self.user_last_login_ip = "never_login"
        self.user_create_time = datetime.now()
        self.user_last_login_time = datetime(1980, 1, 1, 0, 0)
        self.user_token_create_time = datetime(1980, 1, 1, 0, 0)

    def __repr__(self):
        return '<User %r>' % self.username
