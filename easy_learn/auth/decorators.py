from functools import wraps
import jwt
from flask import request, jsonify

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({
                'message': 'Token is missing!!'
            }), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = user_repository.get_by_id(data['_id'])
        except Exception as ex:
            return jsonify({
                'message', str(ex)
            }), 401

        return f(current_user, *args, **kwargs)

    return decorated
