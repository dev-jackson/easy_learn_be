from flask import Blueprint
from easy_learn import users
auth_routes = Blueprint('auth', __name__)

from .decorators import *
from .routers import *