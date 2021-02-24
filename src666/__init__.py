# import src666.app.create
from app import create_app
from database import create_db
from routes import *


app = create_app()
db = create_db(app)
