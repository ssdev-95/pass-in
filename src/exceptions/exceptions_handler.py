from src.http_types.http_response import HTTPResponse
from .exception_types.http_bad_request import HTTPBadRequestException

def exceptions_handler(exception:Exception) -> HTTPResponse:
    if isinstance(exception, HTTPBadRequestException):
        return HTTPResponse(
            body={
                'title': exception.title,
                'errors': [{
                    'message': exception.message
                }]
            },
            status_code=exception.status_code
        )

    return HTTPResponse(body={
        'title': 'Internal Server Error',
        'errors': [
            {
                'message': 'Houston We Have A Problem, Copy',
                'error': f'{exception}'
            },
        ]
    }, status_code=500)
