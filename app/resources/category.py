from flask import Blueprint, jsonify, g
from sqlalchemy.exc import IntegrityError

from app.db import db
from app.models.category import CategoryModel
from app.schemas.category import CategorySchema
from app.schemas.parameter import ParameterSchema
from app.utils.token import token_required
from app.utils.validation import validate_schema

category_blueprint = Blueprint('category_blueprint', __name__)


@category_blueprint.route('', methods=['POST'])
@token_required
@validate_schema(CategorySchema)
def create_category():
    try:
        new_category = CategoryModel(**g.data)
        db.session.add(new_category)
        db.session.commit()
        return jsonify(CategorySchema().dump(new_category)), 201
    except IntegrityError:
        return jsonify(message='Bad Request', error="Category name already exists."), 400


@category_blueprint.route('', methods=['GET'])
@validate_schema(ParameterSchema)
def get_categories():
    total_categories = CategoryModel.query.count()
    categories = CategoryModel.query.offset(g.data['offset']).limit(g.data['limit']).all()
    return jsonify(total_categories=total_categories, categories=CategorySchema(many=True).dump(categories))


@category_blueprint.route('/<category_id>', methods=['GET'])
def get_category_by_id(category_id):
    category = CategoryModel.query.get(category_id)
    if not category:
        return jsonify(message='Category not found'), 404
    return jsonify(CategorySchema().dump(category))
