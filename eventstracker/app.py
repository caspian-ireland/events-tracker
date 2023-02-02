import flask
import dotenv
from flask import make_response, render_template
from .assets import compile_assets
from .auth import auth as auth_blueprint
from .main import main as main_blueprint
from .simulate_errors import simulate_error as sim_error_blueprint

from .extensions import csrf_protect, db, login_manager, assets

dotenv.load_dotenv(".env")


def create_app():
    app = flask.Flask(__name__.split(".")[0])
    app.config.from_object("eventstracker.config.DevelopmentConfig")

    register_extensions(app)
    register_blueprints(app)
    register_error_handlers(app)

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
    app.register_blueprint(sim_error_blueprint)
    return None


def register_error_handlers(app):
    @app.errorhandler(400)
    def bad_request(e):
        """Bad request."""
        return make_response(render_template("errors/400.jinja2"), 400)

    @app.errorhandler(401)
    def unauthorized(e):
        """Unauthorized"""
        return make_response(render_template("errors/401.jinja2"), 401)

    # 403 - Forbidden
    @app.errorhandler(403)
    def forbidden(e):
        """Forbidden."""
        return make_response(render_template("errors/403.jinja2"), 403)

    @app.errorhandler(404)
    def not_found(e):
        """Page not found."""
        return make_response(render_template("errors/404.jinja2"), 404)

    @app.errorhandler(500)
    def server_error(e):
        """Internal server error."""
        return make_response(render_template("errors/500.jinja2"), 500)
