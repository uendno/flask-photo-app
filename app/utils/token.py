from datetime import datetime, timedelta
from functools import wraps

import jwt
from flask import request, jsonify, g

from app.config import config
from app.models.user import UserModel


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        if 'Authorization' in request.headers and request.headers['Authorization']:
            access_token = request.headers['Authorization'].split()[1]
        else:
            return jsonify(message='Missing access token'), 401

        try:
            data = decode_token(access_token)
            current_user = UserModel.query.get(data['id'])
            if not current_user:
                return jsonify(message='User not found'), 404
            g.user = current_user
        except jwt.PyJWTError:
            return jsonify(message='Invalid access token'), 401

        return f(*args, **kwargs)

    return decorator


def encode_token(payload):
    payload = {**payload, 'iat': datetime.utcnow(), 'exp': datetime.utcnow() + timedelta(days=1)}
    return jwt.encode(payload, config.SECRET_KEY)


def decode_token(access_token):
    return jwt.decode(access_token, config.SECRET_KEY)
