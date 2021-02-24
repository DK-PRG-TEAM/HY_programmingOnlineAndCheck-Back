from src.response_errors.CodeClass import Code
from src.response_errors.StatusCode import *
# 通用
OK                          = Code(code=0, devInfo="成功", msg="成功", status=StatusOK, moreInfo="")
Failed                      = Code(code=1, devInfo="失败", msg="失败", status=StatusInternalServerError, moreInfo="")
ErrInput                    = Code(code=2, devInfo="数据格式不正确", msg="请求参数无效", status=StatusBadRequest, moreInfo="")
ErrDB                       = Code(code=3, devInfo="数据库请求错误", msg="服务器内部错误", status=StatusInternalServerError, moreInfo="")
ErrSysFuncFailed            = Code(code=4, devInfo="内部参数处理错误", msg="服务器内部错误", status=StatusInternalServerError, moreInfo="")
ErrToken                    = Code(code=5, devInfo="Token错误或Token过期", msg="权限验证失败", status=StatusInternalServerError, moreInfo="")
# 登录相关



# Code(code=, devInfo="", msg="", status=StatusInternalServerError, moreInfo="")


