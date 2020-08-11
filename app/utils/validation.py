from functools import wraps

from flask import request, jsonify
from marshmallow import ValidationError

from app.models.category import CategoryModel
from app.models.item import ItemModel


def validate_schema(schema):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                request_data = request.args.to_dict() if request.method == 'GET' else request.get_json()
                data = schema().load(request_data)
            except ValidationError as err:
                return jsonify(message='Bad Request', error=err.messages), 400
            return f(data=data, *args, **kwargs)

        return wrapper

    return decorator


def validate_category(f):
    @wraps(f)
    def wrapper(category_id, *args, **kwargs):
        category = CategoryModel.query.get(category_id)
        if not category:
            return jsonify(message='Category not found'), 404
        return f(category=category, category_id=category_id, *args, **kwargs)

    return wrapper


def validate_item(f):
    @wraps(f)
    def wrapper(item_id, *args, **kwargs):
        item = ItemModel.query.get(item_id)
        if not item:
            return jsonify(message='Item not found'), 404
        return f(item=item, item_id=item_id, *args, **kwargs)

    return wrapper


def validate_ownership(f):
    @wraps(f)
    def wrapper(item, user, *args, **kwargs):
        if item.user_id != user.id:
            return jsonify(message='The user is not authorized to perform this action'), 403
        return f(item=item, user=user, *args, **kwargs)

    return wrapper
