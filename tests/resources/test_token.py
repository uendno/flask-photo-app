from unittest.mock import patch

import flask

from app import create_app
from app.utils import token
from tests.utils.token import get_access_token


def test_missing_access_token():
    response = mock_header_and_test_token(None)
    assert response == 401


def test_invalid_token():
    response = mock_header_and_test_token(f'Bearer iikshf92.oifhsfds.98dfdsfh')
    assert response == 401


def test_valid_token(client):
    access_token = get_access_token(client)
    response = mock_header_and_test_token(f'Bearer {access_token}')
    assert response == 200


def mock_header_and_test_token(access_token):
    with patch.object(flask, 'request') as request_mock:
        request_mock.headers.get.return_value = access_token
        with create_app().app_context():
            response = token.token_required(lambda value: (value, 200))()

    request_mock.headers.get.assert_called_once_with('Authorization', None)
    return response[1]
