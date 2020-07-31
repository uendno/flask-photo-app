import os
from flask import Flask
from flask_cors import CORS
from db import db
from app.resources.user import user_blueprint
from app.resources.auth import auth_blueprint

app = Flask(__name__)
CORS(app)

environment_configuration = os.environ['CONFIGURATION_SETUP']
app.config.from_object(environment_configuration)

app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(user_blueprint, url_prefix='/users')
app.register_blueprint(auth_blueprint, url_prefix='/auth')


@app.before_first_request
def init_db():
    db.create_all()


if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=app.config['DEBUG'])
