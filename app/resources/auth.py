from flask import Blueprint, jsonify, g
from werkzeug.security import check_password_hash

from app.models.user import UserModel
from app.schemas.auth import AuthSchema
from app.schemas.user import UserSchema
from app.utils.token import encode_token
from app.utils.validation import validate_schema

auth_blueprint = Blueprint('auth_blueprint', __name__)


@auth_blueprint.route('', methods=['POST'])
@validate_schema(AuthSchema, 'Invalid email or password')
def authenticate_user():
    user = UserModel.query.filter_by(email=g.data['email']).one_or_none()

    if user and check_password_hash(user.password, g.data['password']):
        payload = UserSchema(exclude=('password',)).dump(user)
        encoded_jwt = encode_token(payload)
        return jsonify(access_token=encoded_jwt.decode('UTF-8')), 200
    else:
        return jsonify(message='Invalid email or password'), 400
