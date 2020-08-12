from marshmallow import Schema, fields, validate


class CreateUserSchema(Schema):
    name = fields.String(validate=validate.Length(min=1, max=30), required=True)
    email = fields.Email(validate=validate.Length(max=30), required=True, load_only=True)
    password = fields.String(validate=validate.Length(min=6), required=True, load_only=True)


class GetUserSchema(CreateUserSchema):
    id = fields.Integer()
