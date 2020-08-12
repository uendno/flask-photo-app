from werkzeug.security import generate_password_hash

from app.db import db
from .base import BaseModel
from .item import ItemModel


class UserModel(BaseModel):
    __tablename__ = 'user'

    name: str = db.Column(db.String(30))
    email: str = db.Column(db.String(30), unique=True)
    hashed_password: str = db.Column(db.String(94))
    items = db.relationship(ItemModel, backref='author', lazy='joined')

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
