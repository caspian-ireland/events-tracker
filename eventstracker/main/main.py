from flask import Blueprint, render_template
from eventstracker.extensions import db

main = Blueprint("main", __name__, template_folder="templates")


@main.route("/")
@main.route("/home")
@main.route("/index")
def index():
    return render_template("index.jinja2")


@main.route("/about")
def about():
    return render_template("about.jinja2")
