from datetime import datetime, timedelta
from functools import wraps

import flask
import jwt

from app.config import config
from app.constants.error_message import MISSING_TOKEN, INVALID_TOKEN
from app.models.user import UserModel
from app.utils.app_exception import AuthenticationException


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        auth_header = flask.request.headers.get('Authorization')
        if not auth_header:
            raise AuthenticationException(MISSING_TOKEN)

        auth_header_split = auth_header.split()
        if len(auth_header_split) != 2 or auth_header_split[0] != 'Bearer':
            raise AuthenticationException(INVALID_TOKEN)

        access_token = auth_header_split[1]

        try:
            data = decode_token(access_token)
            current_user = UserModel.query.get(data['id'])
            if not current_user:
                raise jwt.PyJWTError()
            user = current_user
        except jwt.PyJWTError:
            raise AuthenticationException(INVALID_TOKEN)

        return f(user=user, *args, **kwargs)

    return decorator


def encode_token(payload):
    payload = {**payload, 'iat': datetime.utcnow(), 'exp': datetime.utcnow() + timedelta(days=1)}
    return jwt.encode(payload, config.SECRET_KEY, algorithm='HS256').decode('UTF-8')


def decode_token(access_token):
    return jwt.decode(access_token, config.SECRET_KEY, algorithms=['HS256'])
