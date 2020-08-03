from marshmallow import Schema, fields, validate, validates, ValidationError

from app.models.user import UserModel


class AuthSchema(Schema):
    email = fields.Email(validate=validate.Length(max=30), required=True)
    password = fields.String(validate=validate.Length(min=6), required=True)

    @validates('email')
    def validate_email(self, value):
        if not UserModel.query.filter_by(email=value).one_or_none():
            raise ValidationError('Email not found.')
