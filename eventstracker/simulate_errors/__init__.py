"""
Package for Simulate Errors Blueprint.

This provides routes to make it easy to check status code pages.
"""
import typing
from flask import Blueprint, abort
from flask import current_app as app
import re
import os


simulate_error = Blueprint("simulate_error", __name__, url_prefix="/simulate_error")


def find_supported_codes(templates: typing.List[str]) -> typing.List[int]:
    """Find Supported Codes.

    Takes a list of template files and finds supported HTTP status codes.

    Args:
        templates (typing.List[str]): List of template files.

    Returns:
        typing.List[int]: List of supported HTTP status codes
    """

    # Find files in templates that are in the directory 'errors',
    # have a 3 digit number and the .jinja2 extension.
    error_templates = [
        i
        for i in templates
        if (lambda x: re.search(rf"^errors\{os.sep}\d{{3}}\.jinja2$", x))(i)
    ]

    # Find the 3 digit code from these files. Split into two steps
    # with a None check to stop mypy complaining.
    code_match = [(lambda x: re.search(r"\d{3}", x))(i) for i in error_templates]
    supported_codes = [int(i.group(0)) for i in code_match if i is not None]
    return supported_codes


@simulate_error.route("/<int:code>")
def simulate_error_route(code: int):
    """
    Route for checking status code pages.

    Dynamic routing used to access available status code pages.
    If none found then returns 404 page.
    """

    supported_codes = find_supported_codes(app.jinja_env.list_templates())

    if code in supported_codes:
        abort(code)
    else:
        abort(404)
