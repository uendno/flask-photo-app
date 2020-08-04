from marshmallow import Schema, fields, validate, validates, ValidationError

from app.models.user import UserModel


class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String(validate=validate.Length(min=1, max=30), required=True)
    email = fields.Email(validate=validate.Length(max=30), required=True, load_only=True)
    password = fields.String(validate=validate.Length(min=6), required=True, load_only=True)

    @validates('email')
    def validate_email(self, value):
        if UserModel.query.filter_by(email=value).one_or_none():
            raise ValidationError('Email already exists.')
