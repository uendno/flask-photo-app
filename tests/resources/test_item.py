from tests.utils.request import post, get, put, delete
from tests.utils.token import get_access_token


def test_post_valid_body(client):
    access_token = get_access_token(client)
    body = {
        'description': 'Countryside',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/3/35/Neckertal_20150527-6384.jpg',
    }
    response = post(client, '/categories/1/items', body, access_token)
    assert response.status_code == 201


def test_post_missing_field(client):
    access_token = get_access_token(client)
    body = {'description': 'Countryside'}
    response = post(client, '/categories/1/items', body, access_token)
    assert response.status_code == 400


def test_post_unknown_field(client):
    access_token = get_access_token(client)
    body = {
        'description': 'Countryside',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/3/35/Neckertal_20150527-6384.jpg',
        'title': 'Beautiful countryside'
    }
    response = post(client, '/categories/1/items', body, access_token)
    assert response.status_code == 400


def test_post_empty_field(client):
    access_token = get_access_token(client)
    body = {
        'description': '',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/3/35/Neckertal_20150527-6384.jpg',
    }
    response = post(client, '/categories/1/items', body, access_token)
    assert response.status_code == 400


def test_post_invalid_length(client):
    access_token = get_access_token(client)
    long_name = {
        'description': 'g' * 201,
        'image_url': f'https://googl{"e" * 200}.com',
    }
    response = post(client, '/categories/1/items', long_name, access_token)
    assert response.status_code == 400


def test_post_invalid_category_id(client):
    access_token = get_access_token(client)
    body = {
        'description': 'Countryside',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/3/35/Neckertal_20150527-6384.jpg',
    }
    response = post(client, '/categories/5/items', body, access_token)
    assert response.status_code == 404


def test_get_list_valid_parameters(client):
    response = get(client, '/categories/1/items?offset=2&limit=2')
    assert response.status_code == 200
    assert response.get_json()['total_items'] == 4
    assert len(response.get_json()['items']) == 2


def test_get_list_invalid_parameters(client):
    response = get(client, '/categories/1/items?offset=a')
    assert response.status_code == 400

    response = get(client, '/categories/1/items?limit=-1')
    assert response.status_code == 400


def test_get_list_invalid_category_id(client):
    response = get(client, '/categories/5/items')
    assert response.status_code == 404


def test_get_valid_id(client):
    response = get(client, '/categories/1/items/1')
    assert response.status_code == 200


def test_get_invalid_id(client):
    response = get(client, '/categories/1/items/10')
    assert response.status_code == 404


def test_put_valid_body(client):
    access_token = get_access_token(client)
    body = {
        'description': 'Beach',
        'image_url': 'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/beach-quotes-1559667853.jpg',
    }
    response = put(client, '/categories/1/items/1', body, access_token)
    assert response.status_code == 200
    assert response.get_json()['description'] == body['description']
    assert response.get_json()['image_url'] == body['image_url']


def test_put_invalid_id(client):
    access_token = get_access_token(client)
    body = {
        'description': 'Beach',
        'image_url': 'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/beach-quotes-1559667853.jpg',
    }
    response = put(client, '/categories/1/items/10', body, access_token)
    assert response.status_code == 404


def test_put_invalid_author(client):
    access_token = get_access_token(client)
    body = {
        'description': 'Beach',
        'image_url': 'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/beach-quotes-1559667853.jpg',
    }
    response = put(client, '/categories/1/items/3', body, access_token)
    assert response.status_code == 403


def test_delete_valid_id(client):
    access_token = get_access_token(client)
    response = delete(client, '/categories/1/items/1', access_token)
    assert response.status_code == 200


def test_delete_invalid_id(client):
    access_token = get_access_token(client)
    response = delete(client, '/categories/1/items/10', access_token)
    assert response.status_code == 404


def test_delete_invalid_author(client):
    access_token = get_access_token(client)
    response = delete(client, '/categories/1/items/3', access_token)
    assert response.status_code == 403
