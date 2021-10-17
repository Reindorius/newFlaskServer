from functools import wraps

from flask import jsonify, request


def check_auth(username, password):
    return username == 'admin' and password == 'secret'


def not_authenticated():
    message = {'message': 'Not Authenticated'}
    resp = jsonify(message)

    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Example"'

    return resp


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth:
            return not_authenticated()
        elif not check_auth(auth.username, auth.password):
            return not_authenticated()
        else:
            return f(*args, **kwargs)

    return decorated
