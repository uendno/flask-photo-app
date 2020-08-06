from tests.utils.request import get, post
from tests.utils.token import get_access_token


def test_post_success(client):
    body = {
        "email": "huong@gmail.com",
        "password": "123456",
        "name": "Huong"
    }
    response = post(client, '/users', body)
    assert response.status_code == 201


def test_post_with_duplicate_email(client):
    body = {
        "email": "duong@gmail.com",
        "password": "123456",
        "name": "Duong"
    }
    response = post(client, '/users', body)
    assert response.status_code == 400


def test_get_success(client):
    access_token = get_access_token(client)
    response = get(client, '/users/me', access_token)
    assert response.status_code == 200


def test_get_with_invalid_token(client):
    response = get(client, '/users/me')
    assert response.status_code == 401

    response = get(client, '/users/me', 'test_token')
    assert response.status_code == 401
