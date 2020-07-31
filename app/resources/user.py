from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from werkzeug.security import generate_password_hash
from db import db
from app.models.user import UserModel
from app.schemas.user import UserSchema
from app.utils.token import token_required

user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.route('', methods=['POST'])
def create_user():
    try:
        user_data = UserSchema().load(request.json)
    except ValidationError as err:
        return jsonify(message=err.messages), 400

    hashed_password = generate_password_hash(user_data['password'], method='pbkdf2:sha256', salt_length=8)
    new_user = UserModel(name=user_data['name'], email=user_data['email'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return '', 201


@user_blueprint.route('/me', methods=['GET'])
@token_required
def get_current_user(current_user):
    return jsonify(id=current_user.id, name=current_user.name)
