import json
from flask import request
from . import user_routes


@user_routes.route('/', methods=["GET"])
def users():
    return json.dumps([
        {"1": "2"}
    ])


@user_routes.route('/<int:_id>', methods=['GET'])
def user_by_id(_id):
    print(_id)
    return {"id": _id}


@user_routes.route('/update', methods=['UPDATE'])
def user_update():
    user_data = request.json()
    return user_data


@user_routes.route('/delete/<int:_id>', methods=['DELETE'])
def user_delete(_id):
    return _id
