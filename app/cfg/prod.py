import os

from .base import BaseConfig


class Config(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_ENDPOINT')
