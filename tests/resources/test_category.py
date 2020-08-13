from tests.helpers.request import post, get
from tests.helpers.token import get_access_token


class TestCreateCategory:
    def test_create_category_with_valid_body(self, client):
        access_token = get_access_token(client)
        body = {
            'name': 'Landscape',
            'description': 'Countryside',
            'image_url': 'https://upload.wikimedia.org/wikipedia/commons/3/35/Neckertal_20150527-6384.jpg',
        }
        response = post(client, '/categories', body, access_token)
        assert response.status_code == 201
        assert response.get_json()['name'] == body['name']
        assert response.get_json()['description'] == body['description']
        assert response.get_json()['image_url'] == body['image_url']

    def test_create_category_with_duplicate_name(self, client):
        access_token = get_access_token(client)
        body = {
            'name': 'Spring',
            'description': 'Countryside',
            'image_url': 'https://upload.wikimedia.org/wikipedia/commons/3/35/Neckertal_20150527-6384.jpg',
        }
        response = post(client, '/categories', body, access_token)
        assert response.status_code == 400

    def test_create_category_with_invalid_type(self, client):
        access_token = get_access_token(client)
        body = {
            'name': 123456,
            'description': 123456,
            'image_url': 'upload.wikimedia.org/wikipedia/commons/3/35/Neckertal_20150527-6384.jpg',
        }
        response = post(client, '/categories', body, access_token)
        assert response.status_code == 400

    def test_create_category_with_missing_field(self, client):
        access_token = get_access_token(client)
        body = {
            'name': 'Landscape',
            'description': 'Countryside'
        }
        response = post(client, '/categories', body, access_token)
        assert response.status_code == 400

    def test_create_category_with_unknown_field(self, client):
        access_token = get_access_token(client)
        body = {
            'name': 'Landscape',
            'description': 'Countryside',
            'image_url': 'https://upload.wikimedia.org/wikipedia/commons/3/35/Neckertal_20150527-6384.jpg',
            'title': 'Beautiful countryside'
        }
        response = post(client, '/categories', body, access_token)
        assert response.status_code == 400

    def test_create_category_with_empty_field(self, client):
        access_token = get_access_token(client)
        body = {
            'name': '',
            'description': '',
            'image_url': 'https://upload.wikimedia.org/wikipedia/commons/3/35/Neckertal_20150527-6384.jpg',
        }
        response = post(client, '/categories', body, access_token)
        assert response.status_code == 400

    def test_create_category_with_invalid_length(self, client):
        access_token = get_access_token(client)
        long_name = {
            'name': 'g' * 31,
            'description': 'g' * 201,
            'image_url': f'https://googl{"e" * 200}.com',
        }
        response = post(client, '/categories', long_name, access_token)
        assert response.status_code == 400


class TestGetCategory:
    def test_get_category_with_valid_id(self, client):
        response = get(client, '/categories/1')
        assert response.status_code == 200
        assert response.get_json()['id'] == 1
        assert response.get_json()['name'] == 'Spring'
        assert response.get_json()['description'] == 'Warm'
        assert response.get_json()['image_url'] == 'https://vn.got-it.ai/'

    def test_get_category_with_invalid_id(self, client):
        response = get(client, '/categories/5')
        assert response.status_code == 404

    def test_get_list_category_with_valid_parameters(self, client):
        response = get(client, '/categories?offset=2&limit=2')
        assert response.status_code == 200
        assert response.get_json()['total_items'] == 4
        assert len(response.get_json()['items']) == 2

    def test_get_list_category_with_invalid_parameters(self, client):
        response = get(client, '/categories?offset=a')
        assert response.status_code == 400

        response = get(client, '/categories?limit=-1')
        assert response.status_code == 400
