from flask import Blueprint
from flask_restful import Api
from src.apis import UserApi

api_blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(api_blueprint)

api.add_resource(
    UserApi,
    '/user',
    '/user/',
    '/user/<int:user_id>',
    '/user/<int:user_id>/'
)
