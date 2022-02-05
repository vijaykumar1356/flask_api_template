import os
from dicttoxml import dicttoxml
import requests
from flask import Response
from flask_restful import Resource, fields, reqparse, marshal, abort as api_abort

parser = reqparse.RequestParser()
parser.add_argument('address', type=str, required=True, location='json')
parser.add_argument('output_format', type=str, required=True, location='json')

output_fields = {
    'address': fields.String,
    'coordinates': fields.Raw
}


class URLShortnerAPI(Resource):
    def get(self):
        return {
            'message': 'Hello, This is a GET request'
        }

    def post(self):
        return {
            'message': 'Hello, This is a POST request'
        }
