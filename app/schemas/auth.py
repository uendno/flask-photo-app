from marshmallow import Schema, fields, validate


class AuthSchema(Schema):
    email = fields.Email(validate=validate.Length(max=30), required=True)
    password = fields.String(validate=validate.Length(min=6), required=True)
