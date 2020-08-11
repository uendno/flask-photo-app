from flask import Flask, jsonify
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

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

    app.register_blueprint(user_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(category_blueprint)
    app.register_blueprint(item_blueprint)

    @app.errorhandler(HTTPException)
    def handle_bad_request(e):
        error = str(e)
        return jsonify(message=error), int(error[:3])

    db.init_app(app)
    with app.app_context():
        init_db()
    return app
