from app.db import db

from .item import ItemModel


class CategoryModel(db.Model):
    __tablename__ = 'category'

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(30), unique=True)
    description: str = db.Column(db.String(200))
    image_url: str = db.Column(db.String(200))
    items = db.relationship(ItemModel, backref='category', lazy='joined')
