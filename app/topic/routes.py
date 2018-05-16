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
from .model import Topic
from app.tab.model import Tab
from app.reply.model import Reply
from app.utils import log


@bp.route('/')
def index():
    tabs = Tab.find_all()
    if 'tab' in request.args and request.args.get('tab'):
        tab_title = request.args.get('tab')
        tab = Tab.find_by(title=tab_title)
        topic_list = Topic.find_all(tab_id=tab.id)
    else:
        tab_title = ''
        topic_list = Topic.find_all()
    return render_template('index.html',
                           topic_list=topic_list,
                           tabs=tabs,
                           tab_title=tab_title,
                           token=new_csrf_token())


@bp.route('/topic/add')
@login_required
def add():
    token = new_csrf_token()
    tabs = Tab.find_all()
    return render_template('topic/add.html',
                           token=token, tabs=tabs)


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
    replies = Reply.find_all(topic_id=t.id)
    token = new_csrf_token()
    return render_template('topic/detail.html',
                           token=token,
                           topic=t, replies=replies)


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
    tabs = Tab.find_all()
    log('edit topic:', topic)
    return render_template('topic/add.html',
                           topic=topic, token=token,
                           tabs=tabs)


@bp.route('/topic/update/<int:id>', methods=['POST'])
@login_required
@csrf_required
def update(id):
    form = request.form.to_dict()
    Topic.update(id, **form)
    return redirect(url_for('.detail', id=id))


@bp.route('/images/<filename>')
def image(filename):
    return send_from_directory('images', filename)
