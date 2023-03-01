from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(64))
    first_name = db.Column(db.String(500))
    last_name = db.Column(db.String(500))
    uploads = db.relationship('Upload', backref='user')

class Upload(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    blob = db.Column(db.Text)