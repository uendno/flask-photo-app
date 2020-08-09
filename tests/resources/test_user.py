from tests.utils.request import get, post
from tests.utils.token import get_access_token


def test_get_valid_token(client):
    access_token = get_access_token(client)
    response = get(client, '/users/me', access_token)
    assert response.status_code == 200


def test_post_valid_body(client):
    body = {
        'email': 'huong@gmail.com',
        'password': '123456',
        'name': 'Huong'
    }
    response = post(client, '/users', body)
    assert response.status_code == 201


def test_post_duplicate_email(client):
    body = {
        'email': 'duong@gmail.com',
        'password': '123456',
        'name': 'Duong'
    }
    response = post(client, '/users', body)
    assert response.status_code == 400


def test_post_missing_field(client):
    body = {
        'email': 'huong@gmail.com',
        'password': '123456',
    }
    response = post(client, '/users', body)
    assert response.status_code == 400


def test_post_unknown_field(client):
    body = {
        'email': 'huong@gmail.com',
        'password': '123456',
        'name': 'Huong',
        'user_name': 'huong'
    }
    response = post(client, '/users', body)
    assert response.status_code == 400


def test_post_empty_field(client):
    body = {
        'email': 'huong@gmail.com',
        'password': '123456',
        'name': ''
    }
    response = post(client, '/users', body)
    assert response.status_code == 400


def test_post_invalid_length(client):
    body = {
        'email': f'huon{"g" * 30}@gmail.com',
        'password': '1',
        'name': f'Huon{"g" * 30}'
    }
    response = post(client, '/users', body)
    assert response.status_code == 400
