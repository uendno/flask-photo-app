from tests.utils.request import post, get
from tests.utils.token import get_access_token


def test_post_valid_body(client):
    access_token = get_access_token(client)
    body = {
        'name': 'Landscape',
        'description': 'Countryside',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/3/35/Neckertal_20150527-6384.jpg',
    }
    response = post(client, '/categories', body, access_token)
    assert response.status_code == 201


def test_post_duplicate_name(client):
    access_token = get_access_token(client)
    body = {
        'name': 'Spring',
        'description': 'Countryside',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/3/35/Neckertal_20150527-6384.jpg',
    }
    response = post(client, '/categories', body, access_token)
    assert response.status_code == 400


def test_post_missing_field(client):
    access_token = get_access_token(client)
    body = {
        'name': 'Landscape',
        'description': 'Countryside'
    }
    response = post(client, '/categories', body, access_token)
    assert response.status_code == 400


def test_post_unknown_field(client):
    access_token = get_access_token(client)
    body = {
        'name': 'Landscape',
        'description': 'Countryside',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/3/35/Neckertal_20150527-6384.jpg',
        'title': 'Beautiful countryside'
    }
    response = post(client, '/categories', body, access_token)
    assert response.status_code == 400


def test_post_empty_field(client):
    access_token = get_access_token(client)
    body = {
        'name': '',
        'description': '',
        'image_url': 'https://upload.wikimedia.org/wikipedia/commons/3/35/Neckertal_20150527-6384.jpg',
    }
    response = post(client, '/categories', body, access_token)
    assert response.status_code == 400


def test_post_invalid_length(client):
    access_token = get_access_token(client)
    long_name = {
        'name': 'g' * 31,
        'description': 'g' * 201,
        'image_url': f'https://googl{"e" * 200}.com',
    }
    response = post(client, '/categories', long_name, access_token)
    assert response.status_code == 400


def test_get_valid_id(client):
    response = get(client, '/categories/1')
    assert response.status_code == 200


def test_get_invalid_id(client):
    response = get(client, '/categories/5')
    assert response.status_code == 404


def test_get_list_valid_parameters(client):
    response = get(client, '/categories?offset=2&limit=2')
    assert response.status_code == 200
    assert response.get_json()['total_categories'] == 4
    assert len(response.get_json()['categories']) == 2


def test_get_list_invalid_parameters(client):
    response = get(client, '/categories?offset=a')
    assert response.status_code == 400

    response = get(client, '/categories?limit=-1')
    assert response.status_code == 400
