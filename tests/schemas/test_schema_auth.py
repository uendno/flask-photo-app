from tests.utils.request import post


def test_post_with_missing_field(client):
    response = post(client, '/auth', {"email": "duong@gmail.com"})
    assert response.status_code == 400

    response = post(client, '/auth', {"password": "123456"})
    assert response.status_code == 400


def test_post_with_unknown_field(client):
    credential = {
        "email": "duong@gmail.com",
        "password": "123456",
        "name": "Duong"
    }
    response = post(client, '/auth', credential)
    assert response.status_code == 400
