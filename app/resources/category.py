from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from app.db import db
from app.models.category import CategoryModel
from app.schemas.category import CategorySchema
from app.utils.token import token_required

category_blueprint = Blueprint('category_blueprint', __name__)


@category_blueprint.route('', methods=['POST'])
@token_required
def create_category(current_user):
    try:
        from flask import request
        data = CategorySchema().load(request.get_json())
    except ValidationError as err:
        return jsonify(message=err.messages), 400

    new_category = CategoryModel(**data)
    db.session.add(new_category)
    db.session.commit()
    return jsonify(CategorySchema().dump(new_category)), 201


@category_blueprint.route('', methods=['GET'])
def get_categories():
    offset = 0
    limit = None
    try:
        offset = int(request.args.get('offset')) if 'offset' in request.args else 0
        limit = int(request.args.get('limit')) if 'limit' in request.args else None
        if offset < 0 or (limit and limit < 0):
            raise ValueError()
    except ValueError as err:
        return jsonify(message='Invalid offset or limit'), 400

    total_categories = CategoryModel.query.count()
    categories = CategoryModel.query.offset(offset).limit(limit).all()
    return jsonify(total_categories=total_categories, categories=CategorySchema(many=True).dump(categories))


@category_blueprint.route('/<category_id>', methods=['GET'])
def get_category_by_id(category_id):
    category = CategoryModel.query.get(category_id)
    if not category:
        return jsonify(message='Category not found'), 404
    return jsonify(CategorySchema().dump(category))
