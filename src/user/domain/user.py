from ....main import db  


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key = True)
    first_names = db.Column(db.String(255))
    last_names = db.Column(db.String(255))
    email = db.Column(db.String(255), nullable=False)

    def __init__(self, first_names, last_names, email, password) -> None:
        self.id = id
        self.first_names = first_names
        self.last_names = last_names
        self.email = email
        self.password = password
