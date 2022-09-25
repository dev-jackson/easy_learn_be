from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


from users import user_routes
from auth import auth_routes

# Add routes
app.register_blueprint(user_routes, url_prefix='/user')
app.register_blueprint(auth_routes, url_prefix='/auth')

# Show map urls
print(app.url_map)

if __name__ == '__main__':
    app.run(debug=True)
