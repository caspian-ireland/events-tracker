import flask
import dotenv
from flask import make_response, render_template
from .assets import compile_assets
from eventstracker.auth import auth as auth_blueprint
from eventstracker.main import main as main_blueprint

from eventstracker.extensions import csrf_protect, db, login_manager, assets

dotenv.load_dotenv(".env")


def create_app():
    app = flask.Flask(__name__.split(".")[0])
    app.config.from_object("eventstracker.config.DevelopmentConfig")

    register_extensions(app)
    register_blueprints(app)

    with app.app_context():
        db.create_all()
        compile_assets(assets)

    return app


def register_extensions(app):
    """Register Flask extensions."""
    db.init_app(app)
    csrf_protect.init_app(app)
    login_manager.init_app(app)
    assets.init_app(app)
    login_manager.login_view = "auth.login"
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    return None


def register_error_handlers(app):
    @app.errorhandler(400)
    def bad_request():
        """Bad request."""
        return make_response(render_template("400.html"), 400)

    # 403 - Forbidden
    @app.errorhandler(403)
    def forbidden(e):
        """Forbidden."""
        return make_response(render_template("403.html"), 403)

    @app.errorhandler(404)
    def not_found():
        """Page not found."""
        return make_response(render_template("404.html"), 404)

    @app.errorhandler(405)
    def method_not_allowed(e):
        """Method Not Allowed."""
        return make_response(render_template("405.html"), 405)

    @app.errorhandler(500)
    def server_error():
        """Internal server error."""
        return make_response(render_template("500.html"), 500)
