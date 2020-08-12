from flask import Blueprint, jsonify
from sqlalchemy.exc import IntegrityError

from app.constants.error_message import CATEGORY_NAME_EXIST
from app.db import db
from app.models.category import CategoryModel
from app.schemas.category import CategoryRequestSchema, CategoryResponseSchema
from app.schemas.pagination import PaginationSchema
from app.utils.custom_exception import BadRequestException
from app.utils.token import token_required
from app.utils.validation import validate_schema, validate_category

category_blueprint = Blueprint('category_blueprint', __name__, url_prefix='/categories')


@category_blueprint.route('', methods=['POST'])
@token_required
@validate_schema(CategoryRequestSchema)
def create_category(data, user):
    try:
        new_category = CategoryModel(**data)
        db.session.add(new_category)
        db.session.commit()
        return jsonify(CategoryResponseSchema().dump(new_category)), 201
    except IntegrityError:
        raise BadRequestException(CATEGORY_NAME_EXIST)


@category_blueprint.route('', methods=['GET'])
@validate_schema(PaginationSchema)
def get_categories(data):
    total_categories = CategoryModel.query.count()
    categories = CategoryModel.query.offset(data['offset']).limit(data['limit']).all()
    return jsonify(total_categories=total_categories,
                   categories=CategoryResponseSchema(many=True).dump(categories)), 200


@category_blueprint.route('/<category_id>', methods=['GET'])
@validate_category
def get_category_by_id(category):
    return jsonify(CategoryResponseSchema().dump(category)), 200
