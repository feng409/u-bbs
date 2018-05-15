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
from app.utils import log


@bp.route('/')
def index():
    topic_list = Topic.find_all()
    token = new_csrf_token()
    if 'tab' in request.args:
        tab = request.args.get('tab', 'all')
    return render_template('index.html',
                           topic_list=topic_list,
                           token=token)


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


@bp.route('/topic/<int:id>')
def detail(id):
    t = Topic.get(id)
    token = new_csrf_token()
    return render_template('topic/detail.html', token=token, topic=t)


@bp.route('/topic/delete/<int:id>')
@login_required
@csrf_required
def delete(id):
    Topic.delete(id)
    return redirect(url_for('.index'))


@bp.route('/topic/edit/<int:id>')
@login_required
def edit(id):
    token = new_csrf_token()
    topic = Topic.find_by(id=id)
    log('edit topic:', topic)
    return render_template('topic/add.html', topic=topic, token=token)


@bp.route('/topic/update/<int:id>', methods=['POST'])
@login_required
@csrf_required
def update(id):
    form = request.form.to_dict()
    Topic.update(id, **form)
    return redirect(url_for('.detail', id=id))
