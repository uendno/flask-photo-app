from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash

from app.models.user import UserModel
from app.utils.token import encode_token

auth_blueprint = Blueprint('auth_blueprint', __name__)


@auth_blueprint.route('', methods=['POST'])
def authenticate_user():
    user_data = request.get_json()
    if not user_data['email'] and not ['password']:
        return jsonify(message="Invalid email or password"), 400

    user = UserModel.query.filter_by(email=user_data['email']).one_or_none()

    if not user:
        return jsonify(message="Invalid email or password"), 400

    if check_password_hash(user.password, user_data['password']):
        payload = {'id': user.id, 'name': user.name, 'email': user.email}
        encoded_jwt = encode_token(payload)
        return jsonify(access_token=encoded_jwt.decode('UTF-8')), 200
    else:
        return jsonify(message="Invalid email or password"), 400
