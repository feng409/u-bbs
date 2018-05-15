# coding: utf-8
from flask import (
    render_template,
    flash,
    redirect,
    url_for,
    request
)
from . import bp
from app.common import (
    current_user,
    new_csrf_token,
    csrf_required,
    login_required
)
from .model import Topic


@bp.route('/')
def index():
    return render_template('index.html', name="u14e")


@bp.route('/topic/add')
def add():
    token = new_csrf_token()
    return render_template('topic/add.html', token=token)


@bp.route('/topic/add', methods=['POST'])
@login_required
@csrf_required
def add_post():
    form = request.form.to_dict()
    u = current_user()
    Topic.new(user_id=u.id, **form)
    return redirect(url_for('.index'))

