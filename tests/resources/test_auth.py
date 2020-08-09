from tests.utils.request import post


def test_post_valid_credentials(client):
    credential = {
        'email': 'duong@gmail.com',
        'password': '123456'
    }
    response = post(client, '/auth', credential)
    assert response.status_code == 200


def test_post_invalid_credentials(client):
    invalid_email = {
        'email': 'le@gmail.com',
        'password': '123456'
    }
    response = post(client, '/auth', invalid_email)
    assert response.status_code == 400

    invalid_password = {
        'email': 'duong@gmail.com',
        'password': '1234567'
    }
    response = post(client, '/auth', invalid_password)
    assert response.status_code == 400


def test_post_missing_field(client):
    response = post(client, '/auth', {'email': 'duong@gmail.com'})
    assert response.status_code == 400

    response = post(client, '/auth', {'password': '123456'})
    assert response.status_code == 400


def test_post_unknown_field(client):
    credential = {
        'email': 'duong@gmail.com',
        'password': '123456',
        'name': 'Duong'
    }
    response = post(client, '/auth', credential)
    assert response.status_code == 400
