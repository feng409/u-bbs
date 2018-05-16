# coding: utf-8
from app import db
from app.common.model import CommonMixin


class Reply(CommonMixin, db.Model):
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))

    def __repr__(self):
        return '<Reply {}>'.format(self.content)
