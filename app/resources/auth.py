from flask import Blueprint, jsonify
from werkzeug.security import check_password_hash

from app.models.user import UserModel
from app.schemas.auth import AuthRequestSchema
from app.utils.token import encode_token
from app.utils.validation import validate_schema

auth_blueprint = Blueprint('auth_blueprint', __name__, url_prefix='/auth')


@auth_blueprint.route('', methods=['POST'])
@validate_schema(AuthRequestSchema)
def authenticate_user(data):
    user = UserModel.query.filter_by(email=data['email']).one_or_none()

    if not user or not check_password_hash(user.password, data['password']):
        return jsonify(message='Invalid email or password.'), 400

    encoded_jwt = encode_token({'id': user.id})
    return jsonify(access_token=encoded_jwt), 200
