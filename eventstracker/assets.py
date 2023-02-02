"""Compile static assets."""
from flask import current_app as app
import flask_assets


def compile_assets(assets: flask_assets.Environment) -> None:
    """Configure and build asset bundles."""

    style_bundle = flask_assets.Bundle(
        "src/scss/main.scss",
        filters="scss,cssmin",
        output="dist/css/style.min.css",
        extra={"rel": "stylesheet/css"},
    )

    js_bundle = flask_assets.Bundle(
        "node_modules/jquery/dist/jquery.min.js",
        "node_modules/bootstrap/dist/js/bootstrap.bundle.min.js",
        "src/js/*.js",
        filters="jsmin",
        output="dist/js/main.min.js",
    )

    assets.register("main_styles", style_bundle)
    assets.register("main_js", js_bundle)
