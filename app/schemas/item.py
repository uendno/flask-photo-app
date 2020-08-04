from marshmallow import Schema, fields, validate

from .user import UserSchema


class ItemSchema(Schema):
    id = fields.Integer()
    description = fields.String(validate=validate.Length(min=1, max=200), required=True)
    image_url = fields.Url(validate=validate.Length(max=200), required=True)
    user_id = fields.Integer(load_only=True)
    category_id = fields.Integer()
    author = fields.Nested(UserSchema)
