from flask import Blueprint, jsonify
from sqlalchemy.exc import IntegrityError

from app.db import db
from app.models.category import CategoryModel
from app.models.item import ItemModel
from app.schemas.item import ItemSchema
from app.schemas.parameter import ParameterSchema
from app.utils.token import token_required
from app.utils.validation import validate_schema

item_blueprint = Blueprint('item_blueprint', __name__)


@item_blueprint.route('/<category_id>/items', methods=['POST'])
@token_required
@validate_schema(ItemSchema)
def create_item(data, user, category_id):
    try:
        new_item = ItemModel(**data, category_id=category_id, user_id=user.id)
        db.session.add(new_item)
        db.session.commit()
        return jsonify(ItemSchema().dump(new_item)), 201
    except IntegrityError:
        return jsonify(message='Category not found'), 404


@item_blueprint.route('/<category_id>/items', methods=['GET'])
@validate_schema(ParameterSchema)
def get_items_by_category_id(data, category_id):
    category = CategoryModel.query.get(category_id)
    if not category:
        return jsonify(message='Category not found'), 404
    total_items = len(category.items)

    items = ItemModel.query \
        .filter_by(category_id=category_id) \
        .offset(data['offset']) \
        .limit(data['limit']) \
        .all()
    return jsonify(total_items=total_items, items=ItemSchema(many=True).dump(items)), 200


@item_blueprint.route('/<category_id>/items/<item_id>', methods=['GET'])
def get_item_by_id(category_id, item_id):
    item = ItemModel.query.filter_by(id=item_id, category_id=category_id).one_or_none()
    if not item:
        return jsonify(message='Item not found'), 404
    return jsonify(ItemSchema().dump(item)), 200


@item_blueprint.route('/<category_id>/items/<item_id>', methods=['PUT'])
@token_required
@validate_schema(ItemSchema)
def update_item_by_id(data, user, category_id, item_id):
    item = ItemModel.query.filter_by(id=item_id, category_id=category_id).one_or_none()
    if not item:
        return jsonify(message='Item not found'), 404

    if item.user_id != user.id:
        return jsonify(message='The user is not authorized to perform this action'), 403

    item.description = data['description']
    item.image_url = data['image_url']
    db.session.commit()
    return jsonify(ItemSchema().dump(item)), 200


@item_blueprint.route('/<category_id>/items/<item_id>', methods=['DELETE'])
@token_required
def delete_item_by_id(user, category_id, item_id):
    item = ItemModel.query.filter_by(id=item_id, category_id=category_id).one_or_none()
    if not item:
        return jsonify(message='Item not found'), 404

    if item.user_id != user.id:
        return jsonify(message='The user is not authorized to perform this action'), 403

    db.session.delete(item)
    db.session.commit()
    return jsonify({}), 200
