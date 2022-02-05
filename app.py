from flask import Flask
from flask_restful import Api

from apis import URLShortnerAPI

app = Flask(__name__)
api = Api(app, prefix='/api')

api.add_resource(
    URLShortnerAPI,
    '/get_short_url',
    '/get_short_url/'
)


@app.route('/', methods=['GET'])
def index():
    return {
        'message': 'Hello World'
    }


if __name__ == '__main__':
    app.run(debug=True)
