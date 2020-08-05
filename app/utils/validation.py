from functools import wraps

from flask import request, jsonify, g, make_response
from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest


def validate_schema(schema):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                g.data = schema().load(request.args.to_dict() if request.method == 'GET' else request.get_json())
            except ValidationError as err:
                return jsonify(message='Bad Request', error=err.messages), 400
            except BadRequest as err:
                return make_response(jsonify(message=str(err)), 400)
            return f(*args, **kwargs)

        return wrapper

    return decorator
