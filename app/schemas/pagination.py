from marshmallow import Schema, fields, validate


class PaginationSchema(Schema):
    offset = fields.Integer(validate=validate.Range(min=0), missing=0)
    limit = fields.Integer(validate=validate.Range(min=0), missing=None)
