from flask import Blueprint
from flask_restful import Api
from src.apis import URLShortnerAPI

api_blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(api_blueprint)

api.add_resource(
    URLShortnerAPI,
    '/get_short_url',
    '/get_short_url/'
)
