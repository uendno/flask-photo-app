from flask import Blueprint, jsonify
from werkzeug.security import check_password_hash

from app.models.user import UserModel
from app.schemas.auth import AuthSchema
from app.schemas.user import UserSchema
from app.utils.token import encode_token
from app.utils.validation import validate_schema

auth_blueprint = Blueprint('auth_blueprint', __name__)


@auth_blueprint.route('', methods=['POST'])
@validate_schema(AuthSchema)
def authenticate_user(data):
    user = UserModel.query.filter_by(email=data['email']).one_or_none()

    if user and check_password_hash(user.password, data['password']):
        payload = UserSchema().dump(user)
        encoded_jwt = encode_token(payload).decode('UTF-8')
        return jsonify(access_token=encoded_jwt), 200
    else:
        return jsonify(message='Bad Request', error='Invalid email or password.'), 400
