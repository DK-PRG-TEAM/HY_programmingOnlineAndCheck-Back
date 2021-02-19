from flask import Blueprint, request, render_template
from src2 import db
from src2.modules import User

userBlueprint = Blueprint("user", __name__)


@userBlueprint.route("/regist", methods=["POST", "GET"])
def user_regist():
    db.create_all()
    db.session.add(User(email="test@test.com", password="pass"))
    db.session.commit()
    return "user_regist"
