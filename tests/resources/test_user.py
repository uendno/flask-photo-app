from tests.helpers.request import get, post
from tests.helpers.token import get_access_token


class TestCreateUser:
    def test_create_user_with_valid_body(self, client):
        body = {
            'email': 'huong@gmail.com',
            'password': '123456',
            'name': 'Huong'
        }
        response = post(client, '/users', body)
        assert response.status_code == 201

    def test_create_user_with_duplicate_email(self, client):
        body = {
            'email': 'duong@gmail.com',
            'password': '123456',
            'name': 'Duong'
        }
        response = post(client, '/users', body)
        assert response.status_code == 400

    def test_create_user_with_invalid_type(self, client):
        body = {
            'email': 'duong',
            'password': 123456,
            'name': 1234567
        }
        response = post(client, '/users', body)
        assert response.status_code == 400

    def test_create_user_with_missing_field(self, client):
        body = {
            'email': 'huong@gmail.com',
            'password': '123456',
        }
        response = post(client, '/users', body)
        assert response.status_code == 400

    def test_create_user_with_unknown_field(self, client):
        body = {
            'email': 'huong@gmail.com',
            'password': '123456',
            'name': 'Huong',
            'user_name': 'huong'
        }
        response = post(client, '/users', body)
        assert response.status_code == 400

    def test_create_user_with_empty_field(self, client):
        body = {
            'email': 'huong@gmail.com',
            'password': '123456',
            'name': ''
        }
        response = post(client, '/users', body)
        assert response.status_code == 400

    def test_create_user_with_invalid_length(self, client):
        body = {
            'email': f'huon{"g" * 30}@gmail.com',
            'password': '1',
            'name': f'Huon{"g" * 30}'
        }
        response = post(client, '/users', body)
        assert response.status_code == 400


class TestGetUser:
    def test_get_user_with_valid_token(self, client):
        access_token = get_access_token(client)
        response = get(client, '/users/me', access_token)
        assert response.status_code == 200
        assert response.get_json()['id'] == 1
        assert response.get_json()['name'] == 'Duong Le'
