from flask import Blueprint, jsonify
from sqlalchemy.exc import IntegrityError

from app.constants.error_message import EMAIL_EXIST
from app.models.user import UserModel
from app.schemas.user import CreateUserSchema, GetUserSchema
from app.utils.app_exception import BadRequestException
from app.utils.token import token_required, encode_token
from app.utils.validation import validate_and_load_schema

user_blueprint = Blueprint('user_blueprint', __name__, url_prefix='/users')


@user_blueprint.route('', methods=['POST'])
@validate_and_load_schema(CreateUserSchema)
def create_user(data):
    try:
        user = UserModel(**data)
        user.save()
        encoded_token = encode_token({'id': user.id})
        return jsonify(access_token=encoded_token), 200
    except IntegrityError:
        raise BadRequestException(EMAIL_EXIST)


@user_blueprint.route('/me', methods=['GET'])
@token_required
def get_current_user(user):
    return jsonify(GetUserSchema().dump(user)), 200
