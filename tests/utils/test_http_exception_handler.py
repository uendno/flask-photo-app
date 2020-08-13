from tests.helpers.token import get_access_token


def test_request_with_invalid_body(client):
    access_token = get_access_token(client)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    response = client.post('/categories/1/items', headers=headers, data='{,}')
    assert response.status_code == 400


def test_request_with_invalid_route(client):
    response = client.get('/')
    assert response.status_code == 404


def test_request_with_invalid_method(client):
    response = client.delete('/users')
    assert response.status_code == 405
