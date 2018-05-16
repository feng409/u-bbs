# coding: utf-8
from app import db
from hashlib import md5
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
from app.common.model import CommonMixin
from app.utils import validate_email, log


class User(CommonMixin, db.Model):
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    signature = db.Column(db.Text)
    topics = db.relationship('Topic', backref='author', lazy='dynamic')
    tabs = db.relationship('Tab', backref='author', lazy='dynamic')
    replies = db.relationship('Reply', backref='author', lazy='dynamic')

    def add_default_value(self):
        self.set_password(self.password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @classmethod
    def register(cls, form):
        if not len(form['username']) > 2:
            return None, '用户名长度必须大于2'
        if cls.exist(username=form['username']):
            return None, '用户已经存在'
        if not len(form['password']) > 2:
            return None, '密码太简单'
        if not len(form['email']) > 0 or not validate_email(form['email']):
            return None, '邮件格式不对'

        user = User.new(**form)
        return user, '注册成功，去登录吧'

    @classmethod
    def validate_login(cls, form):
        user = User.exist(username=form['username'])
        if user is None:
            return None
        elif not check_password_hash(user.password, form['password']):
            return None
        return user

    def set_password(self, password):
        """
        设置hash密码
        """
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """
        检查密码
        """
        return check_password_hash(self.password, password)

    def avatar(self, size):
        b = self.email.lower().encode('utf-8')
        digest = md5(b).hexdigest()
        gravatar_url = 'https://www.gravatar.com/avatar'
        return '{}/{}?d=retro&s={}'.format(gravatar_url, digest, size)

