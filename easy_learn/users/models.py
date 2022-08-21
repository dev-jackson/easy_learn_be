from app import db


class User(db.Model):
    __tablename__ = "user"
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), nullable=True)
    password = db.Column(db.String(255), nullable=True)

    def __init__(self, _id, first_name, last_name, email, password):
        self._id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password