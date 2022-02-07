from flask import Blueprint
from flask_restful import Api
from src.apis import URLShortnerAPI, SearchAPI

api_blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(api_blueprint)

api.add_resource(
    URLShortnerAPI,
    '/shortener',
    '/shortener/'
)
api.add_resource(
    SearchAPI,
    '/search',
    '/search/'
)
