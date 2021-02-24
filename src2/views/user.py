from flask import Blueprint, request, render_template, make_response, current_app
from src2 import db
from src2.modules import User
import json
import re
from src2.modules.response import response_succeed, response_failed

userBlueprint = Blueprint("user", __name__)

'''
TODO:
1. 验证用户是否存在
2. 验证密码强度
3. 密码加密为md5
4. 正确的创建token
'''


@userBlueprint.route("/regist/email", methods=["POST"])
def user_regist():
    current_app.logger.info('logged by current_app.logger')
    db.create_all()
    body_data = request.get_data()
    json_data = json.loads(body_data)
    # print(json_data['msg'])
    if 'email' not in json_data or 'password' not in json_data:
        return response_failed(101, "参数过少")
    if re.match(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$', json_data['email']) is None:
        # response_data_object = Response_template(code=0,
        #                                          msg="succeed",
        #                                          data={
        #                                              "数据位1": "成功",
        #                                              "数据位2": "成功",
        #                                          },
        #                                          timestamp=123)
        # response = make_response(json.dumps(response_data_object.__dict__, sort_keys=True, indent=4, separators=(',', ': ')), 200)
        # response.headers["Content-Type"] = "application/json"

        return response_failed(102, "邮箱格式不合法")
    if re.match(r'^[0-9A-Za-z$@$!%*?&.]{6,20}$', json_data['password']) is None:
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
        u = User.query.filter_by(email=json_data['email']).first()
        print(u)
    except Exception:
        return response_failed(code=106, msg="用户成功创建, 但找不到该用户id")
    return response_succeed(None)
