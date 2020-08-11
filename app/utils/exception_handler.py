class BaseExceptionHandler(Exception):
    def __init__(self, message, data, status_code):
        Exception.__init__(self)
        self.body = {'message': message}
        if data is not None:
            self.body['data'] = data
        self.status_code = status_code


class BadRequestException(BaseExceptionHandler):
    def __init__(self, message='Bad Request', data=None):
        super().__init__(message, data, 400)


class AuthenticationException(BaseExceptionHandler):
    def __init__(self, message='Unauthenticated', data=None):
        super().__init__(message, data, 401)


class AuthorizationException(BaseExceptionHandler):
    def __init__(self, message='Forbidden', data=None):
        super().__init__(message, data, 403)


class NotFoundException(BaseExceptionHandler):
    def __init__(self, message='Not Found', data=None):
        super().__init__(message, data, 404)
