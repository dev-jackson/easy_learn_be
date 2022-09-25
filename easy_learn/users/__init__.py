from flask import Blueprint


user_routes = Blueprint('users', __name__)


from .models import *
from .respository import *
from .routers import *