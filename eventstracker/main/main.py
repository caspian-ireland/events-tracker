"""'Main' Blueprint routes"""

from flask import Blueprint, render_template

main = Blueprint("main", __name__, template_folder="templates")


@main.route("/")
@main.route("/home")
@main.route("/index")
def index() -> str:
    """Route for index page."""
    return render_template("index.jinja2")


@main.route("/about")
def about() -> str:
    """Route for about page"""
    return render_template("about.jinja2")
