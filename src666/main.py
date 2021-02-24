from src666 import app
from src666.setting import APP_PORT, APP_DEBUG, APP_HOST
from src666.module.user import User
from src666 import db

if __name__ == '__main__':
    app.run(host=APP_HOST, port=APP_PORT, debug=APP_DEBUG)