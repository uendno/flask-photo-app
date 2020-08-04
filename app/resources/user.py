from flask import Blueprint, jsonify, request
from marshmallow import ValidationError

from app.db import db
from app.models.user import UserModel
from app.schemas.user import UserSchema
from app.utils.token import token_required

user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.route('', methods=['POST'])
def create_user():
    try:
        data = UserSchema().load(request.get_json())
    except ValidationError as err:
        return jsonify(message=err.messages), 400

    new_user = UserModel(data['name'], data['email'], data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({}), 201


@user_blueprint.route('/me', methods=['GET'])
@token_required
def get_current_user(current_user):
    return jsonify(UserSchema(only=('id', 'name')).dump(current_user))
