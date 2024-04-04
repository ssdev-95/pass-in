from .http_bad_request import HTTPBadRequestException

class HTTPConflictException(HTTPBadRequestException):
    def __init__(self, message:str):
        super().__init__(
            message=message,
            title='Conflict',
            status_code=209
        )
        
