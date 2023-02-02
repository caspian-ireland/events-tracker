"""App Configurations."""

import os


class Config(object):
    """
    Base Configuration.

    Note: this is intended to be extended.
    """

    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    ASSETS_DEBUG = False
    ASSETS_AUTO_BUILD = True
    FLASK_DEBUG = os.getenv("FLASK_DEBUG")
    SASS_BIN = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "static",
        "node_modules",
        ".bin",
        "sass",
    )


class ProductionConfig(Config):
    """Production Configuration."""

    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"


class DevelopmentConfig(Config):
    """Development Configuration."""

    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"
    ASSETS_DEBUG = True


class TestingConfig(Config):
    """Testing Configuration."""

    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    TESTING = True
