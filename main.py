from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from user.application import user_respository

app = Flask(__name__)

app.register_blueprint(user_respository.user_routers)


# TODO: add rurl connection this and .env files
db = SQLAlchemy()
db.__init__(app)

if __name__ == '__main__':
    app.run(debug=True)