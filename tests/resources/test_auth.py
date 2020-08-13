from tests.helpers.request import post


class TestAuthentication:
    def test_authenticate_with_valid_credentials(self, client):
        credential = {
            'email': 'duong@gmail.com',
            'password': '123456'
        }
        response = post(client, '/auth', credential)
        assert response.status_code == 200

    def test_authenticate_with_invalid_credentials(self, client):
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

    def test_authenticate_with_invalid_type(self, client):
        body = {
            'email': 'duong',
            'password': 123456
        }
        response = post(client, '/auth', body)
        assert response.status_code == 400

    def test_authenticate_with_missing_field(self, client):
        response = post(client, '/auth', {'email': 'duong@gmail.com'})
        assert response.status_code == 400

        response = post(client, '/auth', {'password': '123456'})
        assert response.status_code == 400

    def test_authenticate_with_unknown_field(self, client):
        body = {
            'email': 'duong@gmail.com',
            'password': '123456',
            'name': 'Duong'
        }
        response = post(client, '/auth', body)
        assert response.status_code == 400
