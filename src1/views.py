from flask import Blueprint, request, render_template

user = Blueprint("user", __name__)

from .modules import Users
from src import db

@user.route("/login",methods=["POST","GET"])
def user_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # 还记不记得我们的
        # from sqlalchemy.orm import sessionmaker
        # Session = sessionmaker(engine)
        # db_sesson = Session()
        # 现在不用了,因为 Flask-SQLAlchemy 也已经为我们做好会话打开的工作
        # 我们在这里做个弊:
        db.session.add(Users(username=username,password=password))
        db.session.commit()

        # 然后再查询,捏哈哈哈哈哈
        user_info = Users.query.filter(Users.username == username and User.password == password).first()
        print(user_info.username)
        if user_info:
            return f"登录成功{user_info.username}"

    return render_template("login.html")

