from .base import BaseConfig


class Config(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/photo_app_test'
