class HTTPBadRequestException(Exception):
    def __init__(self, message:str, title:str='Bad Request', status_code:int=400):
        self.message = message
        self.title = title
        self.status_code = status_code

