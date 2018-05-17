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
    """
    判断通过get请求的token和session里面的token是否一致
    """
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        log('session:', session)
        log('request.args:', request.args)
        if 'token' in session and 'token' in request.args:
            token_session = session['token']
            token_get = request.args['token']
            log('csrf_required: get({}), session({})'.format(token_get,
                                                             token_session))
            if token_get == token_session:
                return func(*args, **kwargs)
            else:
                abort(401)
        else:
            log('csrf_required:', '无token')
            abort(401)

    return wrapper_func    


def new_csrf_token():
    """
    使用session存csrf_token，并将其返回给客户端
    """
    token_session = str(uuid.uuid4())
    session['token'] = token_session
    log('new_csrf_token:', token_session)
    return token_session
