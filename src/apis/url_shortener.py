import os
from pyshorteners import Shortener
from flask import request
from flask_restful import Resource, fields, reqparse, abort as api_abort, marshal

# local imports
from src.extentions import db
from src.models import URL

url_parser = reqparse.RequestParser()
url_parser.add_argument('long_url', type=str, required=True, location='json')

output_fields = {
    'short_url': fields.String,
    'long_url': fields.String,
    'total_clicks': fields.Integer
}


TOKEN = os.environ.get('BITLY_ACCESS_TOKEN')


class URLShortnerAPI(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.url_shortener = Shortener(api_key=TOKEN)

    def get(self):
        try:
            if request.args.get('short_url'):
                short_url = request.args.get('short_url')
                url = URL.query.filter(URL.short == short_url).first_or_404()
                return {
                    'short_url': url.short,
                    'long_url': url.long,
                    'total_clicks': self.url_shortener.bitly.total_clicks(url.short)
                }
            all_data = URL.query.all()
            data = []
            for url in all_data:
                data.append({
                    'short_url': url.short,
                    'long_url': url.long,
                    'total_clicks': self.url_shortener.bitly.total_clicks(url.short)
                })
            return marshal(data, output_fields)

        except Exception as e:
            print(e)
            api_abort(400, message=str(e))

    def post(self):
        try:
            post_data = url_parser.parse_args()
            short_url = self.url_shortener.bitly.short(post_data['long_url'])
            url = URL(long=post_data['long_url'], short=short_url)
            db.session.add(url)
            db.session.commit()
            return {
                'short_url': url.short
            }
        except Exception as e:
            api_abort(400, message=str(e))
