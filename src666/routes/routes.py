from src666 import app
from flask import request
from markupsafe import escape
import json


@app.route('/')
def home():
    return {
        "msg": "ok",
        "code": "0"
    }


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)


@app.route(rule='/json_request_test', methods=['post'])
def json_request_test():
    request_body = request.get_data()
    json_data = json.loads(request_body)
    print(json_data)
    print('msg is:' + json_data['msg'])
    return 'Your request is: ' + str(json_data)
