from flask import Blueprint, jsonify
from sqlalchemy.exc import IntegrityError

from app.db import db
from app.models.user import UserModel
from app.schemas.user import UserSchema
from app.utils.token import token_required
from app.utils.validation import validate_schema

user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.route('', methods=['POST'])
@validate_schema(UserSchema)
def create_user(data):
    try:
        new_user = UserModel(**data)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({}), 201
    except IntegrityError:
        return jsonify(message='Bad Request', error="Email already exists."), 400


@user_blueprint.route('/me', methods=['GET'])
@token_required
def get_current_user(user):
    return jsonify(UserSchema().dump(user))
