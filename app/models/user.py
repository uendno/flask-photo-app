from app.db import db
from dataclasses import dataclass


@dataclass
class UserModel(db.Model):
    __tablename__ = 'user'

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(30))
    email: str = db.Column(db.String(30), unique=True)
    password: str = db.Column(db.String(94))
