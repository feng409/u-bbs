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
    image = db.Column(db.String(250))
    topics = db.relationship('Topic', backref='author', lazy='dynamic')
    tabs = db.relationship('Tab', backref='author', lazy='dynamic')
    replies = db.relationship('Reply', backref='author', lazy='dynamic')
    message_sent = db.relationship('Message',
                                   foreign_keys='Message.sender_id',
                                   backref='sender', lazy='dynamic')
    message_received = db.relationship('Message',
                                       foreign_keys='Message.receiver_id',
                                       backref='receiver', lazy='dynamic')

    def add_default_value(self):
        self.set_password(self.password)
        self.image = self.avatar()

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

    def change_password(self, new_pass):
        """
        修改密码
        """
        User.update(self.id, password=generate_password_hash(new_pass))

    def avatar(self, size=48):
        b = self.email.lower().encode('utf-8')
        digest = md5(b).hexdigest()
        gravatar_url = 'https://www.gravatar.com/avatar'
        return '{}/{}?d=retro&s={}'.format(gravatar_url, digest, size)

    def recent_create_topics(self):
        """
        创建的主题
        """
        from app.topic.model import Topic
        topics = Topic.query.filter_by(deleted=False, user_id=self.id)\
            .order_by(Topic.updated_time.desc()).all()
        return topics

    def recent_join_topics(self):
        """
        参与的主题，只有回复主题才有效
        """
        from app.topic.model import Topic
        from app.reply.model import Reply
        query = Topic.query.join(
            Reply, Topic.id == Reply.topic_id).filter(
            Reply.user_id == self.id).filter_by(
            deleted=False).order_by(
            Topic.updated_time.desc())
        topics = query.all()
        return topics
