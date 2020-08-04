from werkzeug.security import generate_password_hash

from app.db import db
from .item import ItemModel


class UserModel(db.Model):
    __tablename__ = 'user'

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(30))
    email: str = db.Column(db.String(30), unique=True)
    password: str = db.Column(db.String(94))
    items = db.relationship(ItemModel, backref='author', lazy='joined')

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
