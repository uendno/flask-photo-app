class Config:
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'mysql+pymysql://root:123456@localhost/photo-app'
    SECRET_KEY = "9as8df(*S*8(das0ˆSˆD%5a67900SA(D*00"


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True


class TestingConfig(DevelopmentConfig):
    TESTING = True


class ProductionConfig(Config):
    pass
