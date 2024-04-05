from typing import Dict

class HttpResponse:
    def __init__(self, body: Dict, statusCode: int) -> None:
        self.body = body
        self.statusCode = statusCode
