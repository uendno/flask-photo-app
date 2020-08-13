from tests.helpers.request import post, get, put, delete
from tests.helpers.token import get_access_token


class TestCreateItem:
    def test_create_item_with_valid_body(self, client):
        access_token = get_access_token(client)
        body = {
            'description': 'Countryside',
            'image_url': 'https://upload.wikimedia.org/wikipedia/commons/3/35/Neckertal_20150527-6384.jpg',
        }
        response = post(client, '/categories/1/items', body, access_token)
        assert response.status_code == 201
        assert response.get_json()['description'] == body['description']
        assert response.get_json()['image_url'] == body['image_url']

    def test_create_item_with_invalid_type(self, client):
        access_token = get_access_token(client)
        body = {
            'description': 1234567,
            'image_url': 'upload.wikimedia.org/wikipedia/commons/3/35/Neckertal_20150527-6384.jpg',
        }
        response = post(client, '/categories/1/items', body, access_token)
        assert response.status_code == 400

    def test_create_item_with_missing_field(self, client):
        access_token = get_access_token(client)
        body = {'description': 'Countryside'}
        response = post(client, '/categories/1/items', body, access_token)
        assert response.status_code == 400

    def test_create_item_with_unknown_field(self, client):
        access_token = get_access_token(client)
        body = {
            'description': 'Countryside',
            'image_url': 'https://upload.wikimedia.org/wikipedia/commons/3/35/Neckertal_20150527-6384.jpg',
            'title': 'Beautiful countryside'
        }
        response = post(client, '/categories/1/items', body, access_token)
        assert response.status_code == 400

    def test_create_item_with_empty_field(self, client):
        access_token = get_access_token(client)
        body = {
            'description': '',
            'image_url': 'https://upload.wikimedia.org/wikipedia/commons/3/35/Neckertal_20150527-6384.jpg',
        }
        response = post(client, '/categories/1/items', body, access_token)
        assert response.status_code == 400

    def test_create_item_with_invalid_length(self, client):
        access_token = get_access_token(client)
        long_name = {
            'description': 'g' * 201,
            'image_url': f'https://googl{"e" * 200}.com',
        }
        response = post(client, '/categories/1/items', long_name, access_token)
        assert response.status_code == 400

    def test_create_item_with_invalid_category_id(self, client):
        access_token = get_access_token(client)
        body = {
            'description': 'Countryside',
            'image_url': 'https://upload.wikimedia.org/wikipedia/commons/3/35/Neckertal_20150527-6384.jpg',
        }
        response = post(client, '/categories/5/items', body, access_token)
        assert response.status_code == 404


class TestGetItem:
    def test_get_item_with_valid_id(self, client):
        response = get(client, '/categories/1/items/1')
        assert response.status_code == 200
        assert response.get_json()['id'] == 1
        assert response.get_json()['description'] == 'Plant'
        assert response.get_json()['image_url'] == 'https://vn.got-it.ai/'
        assert response.get_json()['category_id'] == 1
        assert response.get_json()['author']['id'] == 1
        assert response.get_json()['author']['name'] == 'Duong Le'

    def test_get_item_with_invalid_id(self, client):
        response = get(client, '/categories/1/items/10')
        assert response.status_code == 404

    def test_get_list_item_with_valid_parameters(self, client):
        response = get(client, '/categories/1/items?offset=2&limit=2')
        assert response.status_code == 200
        assert response.get_json()['total_items'] == 4
        assert len(response.get_json()['items']) == 2

    def test_get_list_item_with_invalid_parameters(self, client):
        response = get(client, '/categories/1/items?offset=a')
        assert response.status_code == 400

        response = get(client, '/categories/1/items?limit=-1')
        assert response.status_code == 400

    def test_get_list_item_with_invalid_category_id(self, client):
        response = get(client, '/categories/5/items')
        assert response.status_code == 404


class TestUpdateItem:
    def test_update_item_with_valid_body(self, client):
        access_token = get_access_token(client)
        body = {
            'description': 'Beach',
            'image_url': 'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/beach-quotes-1559667853.jpg',
        }
        response = put(client, '/categories/1/items/1', body, access_token)
        assert response.status_code == 200
        assert response.get_json()['description'] == body['description']
        assert response.get_json()['image_url'] == body['image_url']

    def test_update_item_with_invalid_id(self, client):
        access_token = get_access_token(client)
        body = {
            'description': 'Beach',
            'image_url': 'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/beach-quotes-1559667853.jpg',
        }
        response = put(client, '/categories/1/items/10', body, access_token)
        assert response.status_code == 404

    def test_update_item_with_invalid_author(self, client):
        access_token = get_access_token(client)
        body = {
            'description': 'Beach',
            'image_url': 'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/beach-quotes-1559667853.jpg',
        }
        response = put(client, '/categories/1/items/3', body, access_token)
        assert response.status_code == 403


class TestDeleteItem:
    def test_delete_item_with_valid_id(self, client):
        access_token = get_access_token(client)
        response = delete(client, '/categories/1/items/1', access_token)
        assert response.status_code == 200

    def test_delete_item_with_invalid_id(self, client):
        access_token = get_access_token(client)
        response = delete(client, '/categories/1/items/10', access_token)
        assert response.status_code == 404

    def test_delete_item_with_invalid_author(self, client):
        access_token = get_access_token(client)
        response = delete(client, '/categories/1/items/3', access_token)
        assert response.status_code == 403
