import pytest

from app import create_app
from app.db import db, clear_db
from .utils.db import insert_test_data


@pytest.fixture
def client():
    app = create_app()

    with app.test_client() as client:
        with app.app_context():
            insert_test_data(db)
        yield client

    with app.app_context():
        clear_db()
