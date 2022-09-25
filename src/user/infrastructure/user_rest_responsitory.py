from crypt import crypt
import json
from flask import Blueprint, request, make_response
from user.domain.user import db 

user_routes = Blueprint('user')

def create(user):
    try:
        db.session.add(user)
        db.session.commit()
    except:
        return make_response({
            "code": 404,
            "message": "Error to create user"
        })
    
    return make_response(json.dump({
        "code": 200,
        "message": "User susefully create",
    }))
