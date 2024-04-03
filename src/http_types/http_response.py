from typing import Dict
from flask import jsonify

class HTTPResponse:
    def __init__(self, body:Dict, status_code:int=200) -> None:
        self.body = body
        self.status_code = status_code

    def __json__(self):
        json = {}

        if self.body is not None:
            json = self.body

        return jsonify(json)
