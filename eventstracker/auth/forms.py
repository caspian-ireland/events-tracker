"""Auth - WTF Forms."""
import flask_wtf
import wtforms
from wtforms import validators


class LoginForm(flask_wtf.FlaskForm):
    """
    Login Form.

    Handles form and validation for email, password and submit button.
    """

    email = wtforms.StringField(
        "Email", validators=[validators.DataRequired(), validators.Email()]
    )
    password = wtforms.PasswordField("Password", validators=[validators.DataRequired()])
    submit = wtforms.SubmitField("Login")


class SignUpForm(flask_wtf.FlaskForm):
    """
    Signup Form.

    Handles form and validation for name, email, password,
    confirm_password and submit button.
    """

    name = wtforms.StringField("Name", validators=[validators.DataRequired()])
    email = wtforms.StringField(
        "Email", validators=[validators.DataRequired(), validators.Email()]
    )
    password = wtforms.PasswordField("Password", validators=[validators.DataRequired()])
    confirm_password = wtforms.PasswordField(
        "Confirm Password",
        validators=[
            validators.DataRequired(),
            validators.EqualTo("password", message="Passwords don't match!"),
        ],
    )
    submit = wtforms.SubmitField("Sign Up")
