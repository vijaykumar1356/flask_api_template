import os
from pyshorteners import Shortener
from flask import request
from flask_restful import Resource, fields, reqparse, abort as api_abort

url_parser = reqparse.RequestParser()
url_parser.add_argument('url', type=str, required=True, location='json')

output_fields = {
    'short_url': fields.String
}

TOKEN = os.environ.get('BITLY_ACCESS_TOKEN')


class URLShortnerAPI(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.url_shortener = Shortener(api_key=TOKEN)

    def get(self):
        try:
            short_url = request.args.get('short_url')
            if short_url:
                return {
                    'total_clicks': self.url_shortener.bitly.total_clicks(short_url),
                    'short_url': short_url
                }
            return {
                'message': 'short url not provided in request params'
            }
        except Exception as e:
            print(e)
            api_abort(400, message=str(e))

    def post(self):
        try:
            post_data = url_parser.parse_args()
            short_url = self.url_shortener.bitly.short(post_data['url'])
            return {
                'short_url': short_url
            }
        except Exception as e:
            api_abort(400, message=str(e))
