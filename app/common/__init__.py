# coding: utf-8
from flask import session, request
from app.user.model import User
from app.utils import log


def current_user():
    if 'user_id' in session:
        uid = int(session['user_id'])
        e = User.exist(id=uid)
        log('current_user', e)
        return e
    else:
        return None
