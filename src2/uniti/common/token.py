from flask import request, current_app  # current可以自动寻找到app对象
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


def creat_token(user_id):
    """
    创建token
    :param user_id: 用户id
    :return: token字符串
    """
    serializer = Serializer(current_app.config["SECRET_KEY"], expires_in=3600)
    token = serializer.dumps({"id": user_id}).decode("ascii")
    return token


def verify_token(token: str):
    """
    验证token
    :param token: token字符串
    :return: 用户id or None
    """
    serializer = Serializer(current_app.config["SECRET_KEY"])
    try:
        data = serializer.loads(token)  # 尝试解密到字典
    except Exception:
        return None
    return data["id"]


import functools
from src2.modules.response import response_failed


def user_login_required(view_func):
    # Python装饰器（decorator）在实现的时候，被装饰后的函数其实已经是另外一个函数了（函数名等函数属性会发生改变），为了不影响，Python的functools包中提供了一个叫wraps的decorator来消除这样的副作用。
    @functools.wraps(view_func)
    def verify_token(*args, **kwargs):  # 函数内的函数会自动执行
        try:
            token = request.headers["token"]
        except Exception:
            # 没有正确的接受到token
            return response_failed(code=400, msg="缺少token")
        serializer = Serializer(current_app.config["SECRET_KEY"])
        try:
            serializer.loads(token)
        except Exception:
            return response_failed(code=401, msg="token已过期")
        return view_func(*args, **kwargs)
    return verify_token
