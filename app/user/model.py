# coding: utf-8
from app import db
from hashlib import md5
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
from app.common.model import CommonMixin


class User(CommonMixin, db.Model):
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    signature = db.Column(db.Text)

    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)
        # 不要存明文密码
        self.set_password(self.password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

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

