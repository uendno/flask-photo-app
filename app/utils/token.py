from flask import request, jsonify
from functools import wraps
import jwt
from config import Config
from app.models.user import UserModel


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        if 'Authorization' in request.headers and request.headers['Authorization']:
            access_token = request.headers['Authorization'].split()[1]
        else:
            return jsonify(message='Missing access token'), 401

        try:
            data = jwt.decode(access_token, Config.SECRET_KEY)
            current_user = UserModel.query.get(data['id'])
            if not current_user:
                return jsonify(message='User not found'), 404
        except jwt.PyJWTError:
            return jsonify(message='Invalid access token'), 401

        return f(current_user, *args, **kwargs)

    return decorator
