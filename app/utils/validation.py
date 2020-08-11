from functools import wraps

from flask import request
from marshmallow import ValidationError

from app.models.category import CategoryModel
from app.models.item import ItemModel
from app.utils.exception_handler import BadRequestException, NotFoundException, AuthorizationException


def validate_schema(schema):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                request_data = request.args.to_dict() if request.method == 'GET' else request.get_json()
                data = schema().load(request_data)
            except ValidationError as err:
                raise BadRequestException(data=err.messages)
            return f(data=data, *args, **kwargs)

        return wrapper

    return decorator


def validate_category(f):
    @wraps(f)
    def wrapper(category_id, *args, **kwargs):
        category = CategoryModel.query.get(category_id)
        if not category:
            raise NotFoundException('Category not found')
        return f(category=category, category_id=category_id, *args, **kwargs)

    return wrapper


def validate_item(f):
    @wraps(f)
    def wrapper(item_id, *args, **kwargs):
        item = ItemModel.query.get(item_id)
        if not item:
            raise NotFoundException('Item not found')
        return f(item=item, item_id=item_id, *args, **kwargs)

    return wrapper


def validate_ownership(f):
    @wraps(f)
    def wrapper(item, user, *args, **kwargs):
        if item.user_id != user.id:
            raise AuthorizationException('The user is not authorized to perform this action')
        return f(item=item, user=user, *args, **kwargs)

    return wrapper
