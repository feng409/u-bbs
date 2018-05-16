# coding: utf-8
import os
from uuid import uuid4
from flask import (
    render_template,
    flash,
    redirect,
    url_for,
    request,
    session,
    abort
)
from app.common import (
    current_user,
    login_required,
    csrf_required,
    new_csrf_token
)
from . import bp
from .model import User
from config import base_dir


@bp.route('/login', methods=['GET', 'POST'])
def login():
    user = current_user()
    if user:
        return redirect('/')

    if request.method == 'POST':
        form = request.form
        u = User.validate_login(form.to_dict())
        if u is not None:
            session['user_id'] = u.id
            session.permanent = True
            return redirect('/')
        else:
            flash('用户名或密码错误')
            return redirect(url_for('.login'))
    else:
        return render_template('user/login.html')


@bp.route('/logout')
def logout():
    if 'user_id' in session:
        session.pop('user_id')
    return redirect(url_for('.login'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    user = current_user()
    if user:
        return redirect('/')

    if request.method == 'POST':
        form = request.form
        u, result = User.register(form.to_dict())
        flash(result)
        if u is not None:
            return redirect(url_for('.register'))
        else:
            return render_template('user/register.html')
    else:
        return render_template('user/register.html')


@bp.route('/user/<username>')
def user(username):
    """
    用户主页
    """
    u = User.find_by(username=username)
    if not u:
        abort(404)
    return render_template('user/detail.html', user=u)


@bp.route('/setting')
@login_required
def setting():
    """
    用户设置页
    """
    return render_template('user/setting.html', token=new_csrf_token())


@bp.route('/change-userinfo', methods=['POST'])
@login_required
@csrf_required
def change_info():
    """
    修改用户信息
    """
    form = request.form.to_dict()
    u = User.find_by(username=form['username'])
    if not u:
        flash('用户名已被占用')
    else:
        flash('用户信息修改成功')
        User.update(u.id, **form)

    return redirect(url_for('.setting'))


@bp.route('/change-password', methods=['POST'])
@login_required
@csrf_required
def change_password():
    u = current_user()
    form = request.form.to_dict()
    if u.check_password(form['old_pass']):
        u.change_password(form['new_pass'])
        flash('密码修改成功')
    else:
        flash('输入的旧密码不一致')

    return redirect(url_for('.setting'))


@bp.route('/image/add', methods=['POST'])
def image_add():
    file = request.files['avatar']
    suffix = file.filename.rsplit('.', 1)[1]
    filename = '{}.{}'.format(str(uuid4()), suffix)
    path = os.path.join('app/images', filename)
    file.save(path)

    u = current_user()
    User.update(u.id, image='/images/{}'.format(filename))
    flash('头像修改成功')

    return redirect(url_for('.setting'))
