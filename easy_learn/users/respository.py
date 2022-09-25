from . import User
from easy_learn import db

def create(user):
    try:
        db.session.add(user)
        db.session.commit()
        return user
    except Exception as ex:
        print(str(ex))


def get_by_id(_id):
    return User.query.filter_by(_id=_id).first()


def get_by_email(email):
    return User.query.filter_by(email=email).first()


def login(email, password):
    user = User.query.filter_by(email=email).first()
    if user.password == password:
        return user
    return None
