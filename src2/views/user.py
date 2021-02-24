from flask import Blueprint, request, render_template, make_response, current_app
from src2 import db
from src2.modules import User
import json
import re
from src2.modules.response import response_succeed, response_failed
from src2.uniti.common.token import creat_token, verify_token
from datetime import datetime
from src2.uniti.common.token import user_login_required

userBlueprint = Blueprint("user", __name__)

'''
TODO:
1. 验证用户是否存在
2. 验证密码强度
3. 密码加密为md5
4. 正确的创建token
'''


def checkMailFormat(email: str) -> bool:
    if re.match(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$', email) is None:
        return False
    return True


def checkPasswordFormat(password: str) -> bool:
    if re.match(r'^[0-9A-Za-z$@$!%*?&.]{6,20}$', password) is None:
        return False
    return True


@userBlueprint.route("/regist/email", methods=["POST"])
def user_regist_email():
    # current_app.logger.info('logged by current_app.logger')
    db.create_all()
    body_data = request.get_data()
    json_data = json.loads(body_data)
    # print(json_data['msg'])
    if 'email' not in json_data or 'password' not in json_data:
        return response_failed(101, "参数过少")
    if checkMailFormat(json_data['email']) is False:
        return response_failed(102, "邮箱格式不合法")
    if checkPasswordFormat(json_data['password']) is False:
        return response_failed(103, "密码不合法")
    if User.query.filter_by(email=json_data['email']).first() is not None:
        return response_failed(104, '用户已存在')
    try:
        db.session.add(User(email=json_data['email'], password=json_data['password']))
        db.session.commit()
    except Exception as e:
        print("数据库用户创建失败:" + e)
        return response_failed(code=105, msg="数据库用户创建失败")

    try:
        u: (User) = User.query.filter_by(email=json_data['email']).first()
        print("userid:" + str(u.id))
    except Exception as e:
        return response_failed(code=106, msg="用户成功创建, 但找不到该用户id")
    try:
        # print(u.email)
        u.hasToken = True
        u.token = str(creat_token(u.id))
        u.user_token_create_time = datetime.now()
        db.session.commit()
    except Exception as e:
        print(e)
        return response_failed(code=107, msg="初始化数据token失败")

    return response_succeed(None)


@userBlueprint.route("/login/email", methods=["POST"])
def user_login_email():
    body_data = request.get_data()
    json_data = json.loads(body_data)
    if 'email' not in json_data or 'password' not in json_data:
        return response_failed(101, "参数过少")
    if checkMailFormat(json_data['email']) is False:
        return response_failed(102, "邮箱格式不合法")
    u: User = User.query.filter_by(email=json_data['email']).first()
    if u is not None:
        if u.password == json_data['password']:
            return response_succeed({
                "token": creat_token(u.id)
            })
        else:
            return response_failed(code=108, msg="密码错误")
    else:
        return response_failed(code=109, msg="用户不存在")


@userBlueprint.route("/request_test", methods=["GET"])
@user_login_required
def test():
    body_data = request.get_data()
    token = request.headers["token"]
    id = verify_token(token)
    if id is None:
        return response_failed(code=110, msg="id解析失败")
    return response_succeed(id)
