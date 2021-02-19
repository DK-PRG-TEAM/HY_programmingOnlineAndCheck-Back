from src import db


class User(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)  # unique唯一的 # nullable能否为空
    hasUsername = db.Column(db.Boolean, default=False)
    nickname = db.Column(db.String(255), nullable=False, default="default_nickname")

    def __int__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username


