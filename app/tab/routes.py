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
from .model import Tab
from app.utils import log


@bp.route('/admin/tab')
@login_required
def index():
    token = new_csrf_token()
    return render_template('tab/index.html',
                           token=token)


@bp.route('/admin/tab/add', methods=['POST'])
@login_required
@csrf_required
def add():
    form = request.form.to_dict()
    u = current_user()
    tab = Tab.new(user_id=u.id, **form)
    flash('新增 [{}] Tab'.format(tab.title))
    return redirect(url_for('.index'))
