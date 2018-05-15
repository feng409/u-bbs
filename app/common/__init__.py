# coding: utf-8
from flask import (
    session,
    request,
    abort,
    redirect,
    url_for
)
from app.user.model import User
from app.utils import log
from functools import wraps
import uuid


def current_user():
    if 'user_id' in session:
        uid = int(session['user_id'])
        e = User.exist(id=uid)
        log('current_user', e)
        return e
    else:
        return None


def login_required(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        u = current_user()
        if u is None:
            return redirect(url_for('user.login'))
        else:
            return func(*args, **kwargs)
    return wrapper_func


csrf_tokens = dict()


def csrf_required(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        token = request.args.get('token')
        u = current_user()
        if token in csrf_tokens and csrf_tokens[token] == u.id:
            csrf_tokens.pop(token)
            return func(*args, **kwargs)
        else:
            abort(401)

    return wrapper_func


def new_csrf_token():
    u = current_user()
    token = str(uuid.uuid4())
    csrf_tokens[token] = u.id if u else ''
    return token
