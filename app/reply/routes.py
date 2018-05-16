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
    csrf_required,
    login_required
)
from .model import Reply
from app.topic.model import Topic
from app.utils import log


@bp.route('/add', methods=['POST'])
@login_required
@csrf_required
def add():
    form = request.form.to_dict()
    u = current_user()
    reply = Reply.new(user_id=u.id, **form)
    Topic.update(reply.topic_id)
    return redirect(url_for('topic.detail', id=form['topic_id']))


@bp.route('/delete/<int:id>')
@login_required
@csrf_required
def delete(id):
    topic_id = request.args.get('topic_id')
    Reply.delete(id)
    log('delete reply id:', id)
    return redirect(url_for('topic.detail', id=topic_id))
