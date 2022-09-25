from crypt import crypt
from flask import Blueprint, request 
from user.domain.user import User
from user.infrastructure import user_rest_responsitory

user_routers = Blueprint('user')

user_routers.route('/create', methods=['POST'])
def create_user():
    result = None
    if request.method == 'POST':
        user = User(
            first_names = request.form['first_names'],
            last_names = request.form['last_names'],
            email = request.form['email'],
            password = crypt(request.form['password'], 'sha256')
        )
        result = user_rest_responsitory.create(user)
    return result