from .request import post


def get_access_token(client, credential=None):
    if credential is None:
        credential = {'email': 'duong@gmail.com', 'password': '123456'}
    response = post(client, '/auth', credential)
    return response.get_json()['access_token']
