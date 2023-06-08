from typing import Dict
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import jsonify, Flask


db = SQLAlchemy()
migrate = Migrate()


class APIException(Exception):
    def __init__(
        self,
        status_code: int = 400,
        message: str = "Error in Processing",
        payload: Dict = {}, *args, **kwargs
    ) -> None:
        self.status_code = status_code
        self.message = message
        self.payload = payload
        Exception.__init__(self, *args, **kwargs)

    def to_dict(self):
        data = self.payload
        data['message'] = self.message
        return data

    def __str__(self) -> str:
        return f'{self.__class__.__name__}:{self.message}'


def handle_api_exception(api_exception: APIException):
    response = jsonify(api_exception.to_dict())
    response.status_code = api_exception.status_code
    return response


def register_error_handlers(app: Flask):
    app.register_error_handler(APIException, handle_api_exception)
