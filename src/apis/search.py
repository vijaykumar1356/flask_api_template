import os
from pyshorteners import Shortener
from flask import request
from flask_restful import Resource, fields, abort as api_abort, marshal

# local imports
from src.models import URL

output_fields = {
    'short_url': fields.String,
    'long_url': fields.String,
    'total_clicks': fields.Integer
}
TOKEN = os.environ.get('BITLY_ACCESS_TOKEN')


class SearchAPI(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.url_shortener = Shortener(api_key=TOKEN)

    def get(self):
        try:
            if request.args.get('keyword'):
                keyword = request.args.get('keyword', '')
                urls = URL.query.filter(
                    (URL.short.ilike(f"%{keyword}%")) |
                    (URL.long.ilike(f"%{keyword}%"))
                ).all()
                data = []
                for url in urls:
                    data.append({
                        'short_url': url.short,
                        'long_url': url.long,
                        'total_clicks': self.url_shortener.bitly.total_clicks(url.short)
                    })
                return marshal(data, output_fields)

            else:
                return {
                    "messagge": "No Data Found"
                }

        except Exception as e:
            api_abort(400, message=str(e))
