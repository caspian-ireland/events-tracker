import os


class Config(object):
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY")


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    TESTING = True
