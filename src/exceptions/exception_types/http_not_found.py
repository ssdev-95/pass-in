from .http_bad_request import HTTPBadRequestException

class HTTPNotFoundException(HTTPBadRequestException):
    def __init__(self, message: str):
        super().__init__(
            message=message,
            title='Not Found',
            status_code=404
        )
