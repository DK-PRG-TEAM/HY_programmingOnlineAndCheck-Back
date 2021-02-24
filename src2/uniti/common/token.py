from flask import request, jsonify, current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


def create_token(user_id):
    """
    生成token
    :param user_id:用户id
    :return: token
    """

    # 第一个参数是内部的私钥，这里写在共用的配置信息里了，如果只是测试可以写死
    # 第二个参数是有效期(秒)
    serializer = Serializer(current_app.config["SECRET_KEY"], expires_in=3600)
    # 接收用户id转换与编码
    token = serializer.dumps({"id": user_id}).decode("ascii")
    return token


from src2.modules import User


def verify_token(token):
    """
    校验token
    :param token:
    :return: 用户信息 or None
    """

    # 参数为私有秘钥，跟上面方法的秘钥保持一致
    s = Serializer(current_app.config["SECRET_KEY"])
    try:
        # 转换为字典
        data = s.loads(token)
    except Exception:
        return None
    # 拿到转换后的数据，根据模型类去数据库查询用户信息
    user = User.query.get(data["id"])
    return user


import functools


def login_required(view_func):
    # Python装饰器（decorator）在实现的时候，被装饰后的函数其实已经是另外一个函数了（函数名等函数属性会发生改变），为了不影响，Python的functools包中提供了一个叫wraps的decorator来消除这样的副作用。
    @functools.wraps(view_func)
    def verify_token(*args, **kwargs): #该函数为自动执行
        try:
            # 在请求头上拿到token
            token = request.headers["z-token"]
        except Exception:
            # 没接收的到token,给前端抛出错误
            # 这里的code推荐写一个文件统一管理。这里为了看着直观就先写死了。
            return jsonify(code=4103, msg='缺少参数token')

        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            s.loads(token)
        except Exception:
            return jsonify(code=4101, msg="登录已过期")

        return view_func(*args, **kwargs)
    return verify_token
