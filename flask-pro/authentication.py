from functools import wraps

from flask import jsonify


def check_auth(username, password):
    return username == 'admin' and password == 'secret'


def authenticate():
    message = {'message': 'Authenticated'}
    resp = jsonify(message)

    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Example"'

    return resp


