"""
Flask blueprint for authentication routes.
"""
import flask
import typing
from flask import render_template
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from eventstracker.auth import forms
from eventstracker.auth import models
from eventstracker.extensions import db
from werkzeug.wrappers.response import Response as WerkResponse

auth = flask.Blueprint("auth", __name__, template_folder="templates")


@auth.route("/signup", methods=["GET", "POST"])
def signup() -> typing.Union[str, WerkResponse]:
    """Signup Route."""

    form = forms.SignUpForm()

    # Check form is valid and sent with 'POST'
    if form.validate_on_submit():

        email = form.email.data
        name = form.name.data
        password = form.password.data

        # If user already exists redirect to signin
        user = models.User.query.filter_by(email=email).first()
        if user:
            flask.flash(
                "Email already taken! Please sign in or use another email address.",
                category="danger",
            )
            return flask.redirect(flask.url_for("auth.signin"))

        # If new user then add to database and redirect to login
        new_user = models.User(
            email=email,
            name=name,
            password=generate_password_hash(password, method="sha256"),
        )

        db.session.add(new_user)
        db.session.commit()

        flask.flash(message="Sign Up Successful!", category="success")
        return flask.redirect(flask.url_for("auth.login"))
    elif form.errors:
        flask.flash(
            message="Error! Please check validation messages and try again.",
            category="danger",
        )
        return render_template("signup.jinja2", form=form)

    return render_template("signup.jinja2", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login() -> typing.Union[str, WerkResponse]:
    """Login Route."""
    form = forms.LoginForm()

    # Check form is valid and sent with 'POST'
    if form.validate_on_submit():

        email = form.email.data
        password = form.password.data

        user = models.User.query.filter_by(email=email).first()

        # Check user exists and password correct
        if not user or not check_password_hash(user.password, password):
            flask.flash(
                "Please check your login details and try again.", category="danger"
            )
            return flask.redirect(flask.url_for("auth.login"))

        else:
            login_user(user)
            flask.flash(message="Sign in successful!", category="success")
            return flask.redirect(flask.url_for("main.index"))

    elif form.errors:
        flask.flash(
            message="Please check your login details and try again.", category="danger"
        )
        return flask.redirect(flask.url_for("auth.login"))

    return render_template("login.jinja2", form=form)


@auth.route("/logout")
@login_required
def logout() -> WerkResponse:
    """Logout Route."""
    logout_user()
    flask.flash(message="Logout successful. ", category="success")
    return flask.redirect(flask.url_for("main.index"))
