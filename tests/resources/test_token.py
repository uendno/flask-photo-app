import flask

from app import create_app
from app.utils import token
from tests.utils.token import get_access_token


def test_missing_access_token(mocker):
    response = mock_header_and_test_token(mocker, None)
    assert response == 401


def test_invalid_token(mocker):
    response = mock_header_and_test_token(mocker, f'Bearer iikshf92.oifhsfds.98dfdsfh')
    assert response == 401


def test_valid_token(mocker, client):
    access_token = get_access_token(client)
    response = mock_header_and_test_token(mocker, f'Bearer {access_token}')
    assert response == 200


def mock_header_and_test_token(mocker, access_token):
    app = create_app()
    request_mock = mocker.patch.object(flask, 'request')
    request_mock.headers.get.return_value = access_token

    with app.app_context():
        response = token.token_required(lambda value: (value, 200))()

    request_mock.headers.get.assert_called_once_with('Authorization', None)
    return response[1]
