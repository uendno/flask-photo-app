from marshmallow import Schema, fields, validate, validates, ValidationError

from app.models.category import CategoryModel


class CategorySchema(Schema):
    id = fields.Integer()
    name = fields.String(validate=validate.Length(min=1, max=30), required=True)
    description = fields.String(validate=validate.Length(min=1, max=200), required=True)
    image_url = fields.Url(validate=validate.Length(max=200), required=True)

    @validates('name')
    def validate_email(self, value):
        if CategoryModel.query.filter_by(name=value).one_or_none():
            raise ValidationError('Category name already exists.')
