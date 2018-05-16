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
from app.message.routes import send_message


def users_from_content(content):
    # 内容 @u14e
    # 如果用户名含有空格 就不行了 @name 123
    from app.user.model import User
    parts = content.split(' ')
    users = []

    for p in parts:
        if p.startswith('@'):
            username = p[1:]
            u = User.find_by(username=username)
            if u:
                users.append(u)

    return users


@bp.route('/add', methods=['POST'])
@login_required
@csrf_required
def add():
    form = request.form.to_dict()
    u = current_user()
    reply = Reply.new(user_id=u.id, **form)
    Topic.update(reply.topic_id)    # 主题更新时间

    # 发送站内消息
    receivers = users_from_content(form['content'])
    send_message(u, receivers,
                 title='你被 {} AT了'.format(u.username),
                 content=form['content'])
    log('sender At message: sender-{}; receivers={}'.format(u, receivers))
    return redirect(url_for('topic.detail', id=form['topic_id']))


@bp.route('/delete/<int:id>')
@login_required
@csrf_required
def delete(id):
    topic_id = request.args.get('topic_id')
    Reply.delete(id)
    log('delete reply id:', id)
    return redirect(url_for('topic.detail', id=topic_id))
