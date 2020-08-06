from functools import wraps

from flask import request, jsonify
from marshmallow import ValidationError


def validate_schema(schema):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                request_data = request.args.to_dict() if request.method == 'GET' else request.get_json()
                data = schema().load(request_data)
            except ValidationError as err:
                return jsonify(message='Bad Request', error=err.messages), 400
            return f(data, *args, **kwargs)

        return wrapper

    return decorator
