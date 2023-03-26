from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(100), unique=True)
    token = db.Column(db.String(100), unique=True)
    host = db.Column(db.String(50))