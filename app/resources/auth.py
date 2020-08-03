from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from werkzeug.security import check_password_hash

from app.models.user import UserModel
from app.schemas.auth import AuthSchema
from app.schemas.user import UserSchema
from app.utils.token import encode_token

auth_blueprint = Blueprint('auth_blueprint', __name__)


@auth_blueprint.route('', methods=['POST'])
def authenticate_user():
    try:
        data = AuthSchema().load(request.get_json())
    except ValidationError as err:
        return jsonify(message="Invalid email or password"), 400

    user = UserModel.query.filter_by(email=data['email']).one_or_none()

    if check_password_hash(user.password, data['password']):
        payload = UserSchema(exclude=('password',)).dump(user)
        encoded_jwt = encode_token(payload)
        return jsonify(access_token=encoded_jwt.decode('UTF-8')), 200
    else:
        return jsonify(message="Invalid email or password"), 400
