from src import app
from src.setting import APP_PORT, APP_DEBUG, APP_HOST
from src.module.user import User
from src import db

if __name__ == '__main__':
    app.run(host=APP_HOST, port=APP_PORT, debug=APP_DEBUG)