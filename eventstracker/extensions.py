"""Application Extensions."""

from __future__ import annotations
import typing
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from eventstracker.auth import models
from flask_assets import Environment

# Create extensions
db = SQLAlchemy()
csrf_protect = CSRFProtect()
login_manager = LoginManager()
assets = Environment()


@login_manager.user_loader
def load_user(user_id: str) -> typing.Union[models.User, None]:
    """Load User.

    Login manager callback to load user from the session.

    Args:
        user_id (str): User ID.

    Returns:
        typing.Union[models.User, None]: User model if found, else None.
    """
    return models.User.query.get(int(user_id))
