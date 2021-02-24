from flask import make_response
import json
from datetime import datetime


class Response_base_class:
    code = int
    msg = str
    timestamp = str

    def __init__(self, code: int, msg: str, timestamp: str):
        self.code = code
        self.msg = msg
        self.timestamp = timestamp


class Response_succeed_class(Response_base_class):
    data = object

    def __init__(self, code: int, msg: str, data: object, timestamp: str):
        super().__init__(code, msg, timestamp)
        self.data = data
        return


class Response_failed_class(Response_base_class):

    def __init__(self, code: int, msg: str, timestamp: str):
        super().__init__(code, msg, timestamp)
        return


def response_succeed(object_data: object = None):
    """
    返回请求正确的请求
    :param object_data: 对象类型的数据
    :return: make_response对象
    """
    response_data_object = None
    if object_data is not None:
        response_data_object = Response_succeed_class(code=0,
                                                      msg="成功",
                                                      timestamp=str(datetime.now()),
                                                      data=object_data)
    else:
        response_data_object = Response_base_class(code=0,
                                                   msg="成功",
                                                   timestamp=str(datetime.now()))
    response = make_response(
        json.dumps(response_data_object.__dict__, sort_keys=False, indent=4, separators=(',', ': '), ), 200
    )
    response.headers["Content-Type"] = "application/json"
    return response


def response_failed(code: int, msg: str):  # TODO: 现在先凑合用, 未来有时间了再用更抽象的
    """
    返回请求错误的请求
    :param code: 错误代码
    :param msg: 错误信息
    :return: make_response创建的对象
    """
    response_data_object = Response_failed_class(code=code,
                                                 msg=msg,
                                                 timestamp=str(datetime.now()))
    response = make_response(
        json.dumps(response_data_object.__dict__, sort_keys=True, indent=4, separators=(',', ': '), ), 400
    )
    response.headers["Content-Type"] = "application/json"
    return response

# def response_failed(Code): # TODO:未来有时间了再用更抽象的
#     """
#     返回请求错误的请求
#     :param Code: Code对象
#     :param msg: 错误信息
#     :return: make_response创建的对象
#     """
#     response_data_object = Response_failed_class(code=Code.code,
#                                                  msg=Code.message,
#                                                  timestamp=str(datetime.now()))
#     # TODO:应该甩一个log, 内容为DevInfo
#     response = make_response(
#         json.dumps(response_data_object.__dict__, sort_keys=True, indent=4, separators=(',', ': '), ), 400
#     )
#     response.headers["Content-Type"] = "application/json"
#     return response
