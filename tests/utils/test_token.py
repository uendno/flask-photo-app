from unittest.mock import patch

import flask
import pytest

from app import create_app
from app.constants.error_message import MISSING_TOKEN, INVALID_TOKEN
from app.utils.app_exception import AuthenticationException
from app.utils.token import token_required, encode_token


def test_request_with_missing_access_token():
    with pytest.raises(AuthenticationException) as exc_info:
        mock_header_and_test_token(None)
    assert str(exc_info.value) == MISSING_TOKEN


def test_request_with_invalid_token():
    with pytest.raises(AuthenticationException) as exc_info:
        mock_header_and_test_token(f'Bearer iikshf92.oifhsfds.98dfdsfh')
    assert str(exc_info.value) == INVALID_TOKEN

    with pytest.raises(AuthenticationException) as exc_info:
        mock_header_and_test_token(f'iikshf92.oifhsfds.98dfdsfh')
    assert str(exc_info.value) == INVALID_TOKEN

    with pytest.raises(AuthenticationException) as exc_info:
        mock_header_and_test_token(f'Bearer iikshf92.oifhsfds 98dfdsfh')
    assert str(exc_info.value) == INVALID_TOKEN


def test_token_with_invalid_user():
    access_token = encode_token({"id": 3})
    with pytest.raises(AuthenticationException) as exc_info:
        mock_header_and_test_token(f'Bearer {access_token}')
    assert str(exc_info.value) == INVALID_TOKEN


def mock_header_and_test_token(access_token):
    with patch.object(flask, 'request') as request_mock:
        request_mock.headers.get.return_value = access_token
        with create_app().app_context():
            response = token_required(lambda value: (value, 200))()

    request_mock.headers.get.assert_called_once_with('Authorization')
    return response[1]
