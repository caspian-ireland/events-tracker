from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from eventstracker.auth import models
from flask_assets import Environment

db = SQLAlchemy()
csrf_protect = CSRFProtect()
login_manager = LoginManager()
assets = Environment()


@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))
