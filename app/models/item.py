from app.db import db

from .base import BaseModel


class ItemModel(BaseModel):
    __tablename__ = 'item'

    description: str = db.Column(db.String(200))
    image_url: str = db.Column(db.String(200))
    user_id: int = db.Column(db.Integer, db.ForeignKey('user.id'), index=True)
    category_id: int = db.Column(db.Integer, db.ForeignKey('category.id'), index=True)

    def update(self, description, image_url):
        self.description = description
        self.image_url = image_url
        db.session.commit()
