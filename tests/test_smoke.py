"""Smoke test added because this repository shipped with none (repocurator
feature 002). It exercises the one thing every route in src/views/user.py
depends on: that the Flask app factory builds without touching a real MySQL
server, and that a token issued by src/uniti/common/token.py can be verified
back to the same user id.

This also pins down a real defect: the app factory only imports cleanly under
the dependency versions declared in this workflow (Flask 1.1.4 /
itsdangerous 1.1.0 / Flask-SQLAlchemy 2.5.1). Installing current Flask pulls
in itsdangerous>=2.2, which removed TimedJSONWebSignatureSerializer -- the
exact class src/uniti/common/token.py imports -- so `pip install flask` alone
makes this test fail at import time.
"""

from src import create_app
from src.uniti.common.token import creat_token, verify_token


def test_app_factory_builds_and_registers_routes():
    app = create_app()
    rules = {str(rule) for rule in app.url_map.iter_rules()}
    assert "/regist/email" in rules
    assert "/login/email" in rules
    assert "/request_test" in rules


def test_token_round_trip():
    app = create_app()
    with app.app_context():
        token = creat_token(42)
        assert verify_token(token) == 42
