"""Auth - Models"""

from eventstracker.extensions import db
from flask_login import UserMixin


# TODO - fix db.Model mypy error
# Known issue: https://github.com/dropbox/sqlalchemy-stubs/issues/76
class User(UserMixin, db.Model):  # type: ignore
    """
    SQLAlchemy user model.

    UserMixin provides functionality for Flask-Login support.
    """

    id = db.Column(
        db.Integer, primary_key=True
    )  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(1000), nullable=False)
