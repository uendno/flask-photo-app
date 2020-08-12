from flask import Blueprint, jsonify
from werkzeug.security import check_password_hash

from app.constants.error_message import INVALID_CREDENTIALS
from app.models.user import UserModel
from app.schemas.auth import AuthenticationSchema
from app.utils.app_exception import BadRequestException
from app.utils.token import encode_token
from app.utils.validation import validate_and_load_schema

auth_blueprint = Blueprint('auth_blueprint', __name__, url_prefix='/auth')


@auth_blueprint.route('', methods=['POST'])
@validate_and_load_schema(AuthenticationSchema)
def authenticate_user(data):
    user = UserModel.query.filter_by(email=data['email']).one_or_none()

    if not user or not check_password_hash(user.hashed_password, data['password']):
        raise BadRequestException(INVALID_CREDENTIALS)

    encoded_token = encode_token({'id': user.id})
    return jsonify(access_token=encoded_token), 200
