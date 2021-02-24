class Code:
    code = None
    message = None
    status = None
    devInfo = None
    moreInfo = None

    def __init__(self, code, msg, status, devInfo, moreInfo):
        self.code = code
        self.devInfo = devInfo
        self.message = msg
        self.status = status
        self.moreInfo = moreInfo
