class AppException(Exception):
    def __init__(self, message, data, status_code):
        self.body = {'message': message}
        if data is not None:
            self.body['data'] = data
        self.status_code = status_code

    def __str__(self):
        return self.body['message']


class BadRequestException(AppException):
    def __init__(self, message='Bad Request', data=None):
        super().__init__(message, data, 400)


class AuthenticationException(AppException):
    def __init__(self, message='Unauthenticated', data=None):
        super().__init__(message, data, 401)


class AuthorizationException(AppException):
    def __init__(self, message='Forbidden', data=None):
        super().__init__(message, data, 403)


class NotFoundException(AppException):
    def __init__(self, message='Not Found', data=None):
        super().__init__(message, data, 404)
