from flask import Blueprint, abort

simulate_error = Blueprint("simulate_error", __name__)


@simulate_error.route("/simulate_error/<int:code>")
def simulate_error_route(code):
    if code in [400, 401, 403, 404, 500]:
        abort(code)
    else:
        abort(404)
