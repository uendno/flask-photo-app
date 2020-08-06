from tests.utils.request import post


def test_post_with_missing_field(client):
    body = {
        "email": "huong@gmail.com",
        "password": "123456",
    }
    response = post(client, '/users', body)
    assert response.status_code == 400


def test_post_with_unknown_field(client):
    body = {
        "email": "huong@gmail.com",
        "password": "123456",
        "name": "Huong",
        "user_Name": "huong"
    }
    response = post(client, '/users', body)
    assert response.status_code == 400


def test_post_with_empty_field(client):
    body = {
        "email": "huong@gmail.com",
        "password": "123456",
        "name": ""
    }
    response = post(client, '/users', body)
    assert response.status_code == 400


def test_post_with_invalid_length(client):
    long_name = {
        "email": "huong@gmail.com",
        "password": "123456",
        "name": "Huongggggggggggggggggggggggggggggggggggggggg"
    }
    response = post(client, '/users', long_name)
    assert response.status_code == 400

    long_email = {
        "email": "huonggggggggggggggggggggggggggg@gmail.com",
        "password": "123456",
        "name": "Huong"
    }
    response = post(client, '/users', long_email)
    assert response.status_code == 400

    short_password = {
        "email": "huong@gmail.com",
        "password": "123",
        "name": "Huong"
    }
    response = post(client, '/users', short_password)
    assert response.status_code == 400
