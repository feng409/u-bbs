# coding: utf-8
from app import db
from app.common.model import CommonMixin


class Tab(CommonMixin, db.Model):
    title = db.Column(db.String(120), nullable=False, unique=True, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    topics = db.relationship('Topic', backref='tab', lazy='dynamic')

    def __repr__(self):
        return '<Topic {}>'.format(self.title)

