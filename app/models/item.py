from app.db import db


class ItemModel(db.Model):
    __tablename__ = 'item'

    id: int = db.Column(db.Integer, primary_key=True)
    description: str = db.Column(db.String(200))
    image_url: str = db.Column(db.String(200))
    user_id: int = db.Column(db.Integer, db.ForeignKey('user.id'))
    category_id: int = db.Column(db.Integer, db.ForeignKey('category.id'))
