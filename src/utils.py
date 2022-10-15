from typing import Optional
from flask import jsonify
from flask_restful import abort


def api_abort(status_code: int, description: Optional[str] = None, **kwargs):
    data = {'description': description}
    data.update(kwargs)
    response = jsonify(data or {'error': 'There was an error'})
    response.status_code = status_code
    abort(response)
