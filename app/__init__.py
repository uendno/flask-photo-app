from flask import Flask
from flask_cors import CORS

from .config import config
from .db import db, init_db
from .resources.auth import auth_blueprint
from .resources.user import user_blueprint


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(config)

    app.register_blueprint(user_blueprint, url_prefix='/users')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    db.init_app(app)
    with app.app_context():
        init_db()
    return app
