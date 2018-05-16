# coding: utf-8
from flask import (
    render_template,
    flash,
    redirect,
    url_for,
    request,
    send_from_directory)
from . import bp
from app.common import (
    current_user,
    new_csrf_token,
    csrf_required,
    login_required
)
from .model import Message


@bp.route('/')
@login_required
def index():
    u = current_user()
    receive_messages = Message.find_all(receiver_id=u.id)
    return render_template('message/index.html',
                           receive_messages=receive_messages)


@bp.route('/detail/<int:id>')
@login_required
def detail(id):
    m = Message.find_by(id=id)
    return render_template('message/detail.html',
                           message=m)


def send_message(sender, receivers, title, content):
    for r in receivers:
        form = dict(
            title=title,
            content=content,
            sender_id=sender.id,
            receiver_id=r.id
        )
        Message.new(**form)
