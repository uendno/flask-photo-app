from app.db import db
from .base import BaseModel
from .item import ItemModel


class CategoryModel(BaseModel):
    __tablename__ = 'category'

    name: str = db.Column(db.String(30), unique=True)
    description: str = db.Column(db.String(200))
    image_url: str = db.Column(db.String(200))
    items = db.relationship(ItemModel, backref='category', lazy='joined')

    def update(self, name, description, image_url):
        self.name = name
        self.description = description
        self.image_url = image_url
        db.session.commit()
