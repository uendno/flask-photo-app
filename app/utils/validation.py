from functools import wraps

from flask import request, jsonify, g
from marshmallow import ValidationError


def validate_schema(schema, message=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                g.data = schema().load(request.args.to_dict() if request.method == 'GET' else request.get_json())
            except ValidationError as err:
                return jsonify(message=(message if message else err.messages)), 400
            return f(*args, **kwargs)

        return wrapper

    return decorator
