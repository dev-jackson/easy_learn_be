from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from easy_learn.users.routers import user_routes
from easy_learn.auth.routers import auth_routes

app = Flask(__name__)
db = SQLAlchemy(app)

# Add routes
app.register_blueprint(user_routes, url_prefix='/user')
app.register_blueprint(auth_routes, url_prefix='/auth')

# Show map urls
print(app.url_map)

if __name__ == '__main__':
    app.run(debug=True)
