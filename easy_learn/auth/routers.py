from flask import Blueprint, request

auth_routes = Blueprint('auth', __name__)


@auth_routes.route('/login', methods=['POST'])
def auth_login():
    user_login = request.json()
    return user_login


@auth_routes.route('/register', methods=['POST'])
def auth_register():
    user_register = request.json()
    return user_register


