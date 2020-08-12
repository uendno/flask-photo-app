from flask import Blueprint, jsonify
from sqlalchemy.exc import IntegrityError

from app.constants.error_message import EMAIL_EXIST
from app.models.user import UserModel
from app.schemas.user import UserRequestSchema, UserResponseSchema
from app.utils.custom_exception import BadRequestException
from app.utils.token import token_required
from app.utils.validation import validate_schema

user_blueprint = Blueprint('user_blueprint', __name__, url_prefix='/users')


@user_blueprint.route('', methods=['POST'])
@validate_schema(UserRequestSchema)
def create_user(data):
    try:
        UserModel(**data).save()
        return jsonify({}), 201
    except IntegrityError:
        raise BadRequestException(EMAIL_EXIST)


@user_blueprint.route('/me', methods=['GET'])
@token_required
def get_current_user(user):
    return jsonify(UserResponseSchema().dump(user)), 200
