from marshmallow import Schema, fields


class AuthenticationSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)
