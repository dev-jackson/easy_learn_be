from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, request, make_response, jsonify
from easy_learn.users import respository as user_repository
from datetime import datetime, timedelta
from easy_learn.users.models import User
import jwt

auth_routes = Blueprint('auth', __name__)


@auth_routes.route('/login', methods=['POST'])
def login():
    auth = request.form

    if not auth or not auth.get('email') or not auth.get('password'):
        return make_response(
            'Cloud not verify',
            401,
            {'WWW-Authenticate': 'Basic realm="Login required!!"'}
        )

    user = user_repository.get_by_email(auth.get('email'))

    if not user:
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate': 'Basic realm ="User does not exist!!"'}
        )

    if check_password_hash(user.password, auth.get('password')):
        token = jwt.encode({
            '_id': user.id,
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, app.config['SECRET_KEY'])

        return make_response(
            jsonify({'token': token.decode('UTF-8')}),
            200
        )

    return make_response(
        'Cloud not verify',
        403,
        {'WWW-Authenticate': 'Basic realm ="Wrong password!!"'}
    )


@auth_routes.route('/register', methods=['POST'])
def register():
    data = request.form

    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')

    user = user_repository.get_by_email(email)

    if not user:
        user_repository.create(
            User(
                id=None,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=generate_password_hash(password)
            )
        )
        return make_response('Successfully register.', 200)
    else:
        return make_response('User already exists. Please Log in', 202)
