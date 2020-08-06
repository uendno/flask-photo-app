from tests.utils.request import post


def test_post_correct_credentials(client):
    credential = {
        "email": "duong@gmail.com",
        "password": "123456"
    }
    response = post(client, '/auth', credential)
    assert response.status_code == 200


def test_post_incorrect_credentials(client):
    incorrect_email = {
        "email": "le@gmail.com",
        "password": "123456"
    }
    response = post(client, '/auth', incorrect_email)
    assert response.status_code == 400

    incorrect_password = {
        "email": "duong@gmail.com",
        "password": "1234567"
    }
    response = post(client, '/auth', incorrect_password)
    assert response.status_code == 400
