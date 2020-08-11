from unittest.mock import patch

import flask

from app import create_app
from app.utils.token import token_required, encode_token


def test_missing_access_token():
    response = mock_header_and_test_token(None)
    assert response == 401


def test_invalid_token():
    response = mock_header_and_test_token(f'Bearer iikshf92.oifhsfds.98dfdsfh')
    assert response == 401

    response = mock_header_and_test_token(f'iikshf92.oifhsfds.98dfdsfh')
    assert response == 401

    response = mock_header_and_test_token(f'Bearer iikshf92.oifhsfds 98dfdsfh')
    assert response == 401


def test_invalid_user():
    access_token = encode_token({"id": 3})
    response = mock_header_and_test_token(f'Bearer {access_token}')
    assert response == 401


def mock_header_and_test_token(access_token):
    with patch.object(flask, 'request') as request_mock:
        request_mock.headers.get.return_value = access_token
        with create_app().app_context():
            response = token_required(lambda value: (value, 200))()

    request_mock.headers.get.assert_called_once_with('Authorization')
    return response[1]
