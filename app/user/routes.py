# coding: utf-8
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
)
from . import bp
from .model import User


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
    u = User.find_by(username=username)
    if not u:
        abort(404)
    return render_template('user/detail.html', user=u)
