from flask import Blueprint, jsonify, g

from app.db import db
from app.models.user import UserModel
from app.schemas.user import UserSchema
from app.utils.token import token_required
from app.utils.validation import validate_schema

user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.route('', methods=['POST'])
@validate_schema(UserSchema)
def create_user():
    new_user = UserModel(**g.data)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({}), 201


@user_blueprint.route('/me', methods=['GET'])
@token_required
def get_current_user():
    return jsonify(UserSchema(only=('id', 'name')).dump(g.user))
