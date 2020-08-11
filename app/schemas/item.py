from marshmallow import Schema, fields, validate

from .user import UserResponseSchema


class ItemRequestSchema(Schema):
    description = fields.String(validate=validate.Length(min=1, max=200), required=True)
    image_url = fields.Url(validate=validate.Length(max=200), required=True)


class ItemResponseSchema(ItemRequestSchema):
    id = fields.Integer()
    category_id = fields.Integer()
    author = fields.Nested(UserResponseSchema)
