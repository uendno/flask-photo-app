from flask import Flask
from flask_cors import CORS

from .config import config
from .db import db, init_db
from .resources.auth import auth_blueprint
from .resources.category import category_blueprint
from .resources.item import item_blueprint
from .resources.user import user_blueprint


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(config)

    app.register_blueprint(user_blueprint, url_prefix='/users')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(category_blueprint, url_prefix='/categories')
    app.register_blueprint(item_blueprint, url_prefix='/categories')

    db.init_app(app)
    with app.app_context():
        init_db()
    return app
