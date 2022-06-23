from flask import Blueprint, jsonify
from sqlalchemy.exc import IntegrityError

from app.constants.error_message import CATEGORY_NAME_EXIST
from app.models.category import CategoryModel
from app.schemas.category import CreateCategorySchema, GetCategorySchema, UpdateCategorySchema
from app.schemas.pagination import PaginationSchema
from app.utils.app_exception import BadRequestException
from app.utils.token import token_required
from app.utils.validation import validate_and_load_schema, validate_and_load_category, validate_category_ownership

category_blueprint = Blueprint('category_blueprint', __name__, url_prefix='/categories')


@category_blueprint.route('', methods=['POST'])
@token_required
@validate_and_load_schema(CreateCategorySchema)
def create_category(data, user):
    try:
        new_category = CategoryModel(**data)
        new_category.user_id = user.id
        new_category.save()
        return jsonify(GetCategorySchema().dump(new_category)), 201
    except IntegrityError:
        raise BadRequestException(CATEGORY_NAME_EXIST)


@category_blueprint.route('', methods=['GET'])
@validate_and_load_schema(PaginationSchema)
def get_categories(data):
    total_categories = CategoryModel.query.count()
    categories = CategoryModel.query.offset(data['offset']).limit(data['limit']).all()
    return jsonify(total_items=total_categories, items=GetCategorySchema(many=True).dump(categories)), 200


@category_blueprint.route('/<category_id>', methods=['GET'])
@validate_and_load_category
def get_category_by_id(category):
    return jsonify(GetCategorySchema().dump(category)), 200


@category_blueprint.route('/<category_id>', methods=['PUT'])
@token_required
@validate_and_load_schema(UpdateCategorySchema)
@validate_and_load_category
@validate_category_ownership
def update_category_by_id(category, user, data):
    category.update(**data)
    return jsonify(UpdateCategorySchema().dump(category)), 200

@category_blueprint.route('/<category_id>', methods=['DELETE'])
@token_required
@validate_and_load_category
@validate_category_ownership
def delete_category_by_id(category, user):
    category.delete()
    return jsonify({}), 200
