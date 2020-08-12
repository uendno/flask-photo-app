from flask import Blueprint, jsonify

from app.models.item import ItemModel
from app.schemas.item import CreateItemSchema, UpdateItemSchema, GetItemSchema
from app.schemas.pagination import PaginationSchema
from app.utils.token import token_required
from app.utils.validation import validate_and_load_schema, validate_and_load_category, validate_and_load_item, \
    validate_ownership

item_blueprint = Blueprint('item_blueprint', __name__, url_prefix='/categories/<category_id>/items')


@item_blueprint.route('', methods=['POST'])
@token_required
@validate_and_load_schema(CreateItemSchema)
@validate_and_load_category
def create_item(category, data, user):
    new_item = ItemModel(**data, category_id=category.id, user_id=user.id)
    new_item.save()
    return jsonify(GetItemSchema().dump(new_item)), 201


@item_blueprint.route('', methods=['GET'])
@validate_and_load_schema(PaginationSchema)
@validate_and_load_category
def get_items_by_category_id(category, data):
    total_items = len(category.items)
    items = ItemModel.query \
        .filter_by(category_id=category.id) \
        .offset(data['offset']) \
        .limit(data['limit']) \
        .all()
    return jsonify(total_items=total_items, items=GetItemSchema(many=True).dump(items)), 200


@item_blueprint.route('/<item_id>', methods=['GET'])
@validate_and_load_item
def get_item_by_id(item, category_id):
    return jsonify(GetItemSchema().dump(item)), 200


@item_blueprint.route('/<item_id>', methods=['PUT'])
@token_required
@validate_and_load_schema(UpdateItemSchema)
@validate_and_load_item
@validate_ownership
def update_item_by_id(item, data, user, category_id):
    item.update(**data)
    return jsonify(UpdateItemSchema().dump(item)), 200


@item_blueprint.route('/<item_id>', methods=['DELETE'])
@token_required
@validate_and_load_item
@validate_ownership
def delete_item_by_id(item, user, category_id):
    item.delete()
    return jsonify({}), 200
