# coding: utf-8
from app import db
from app.common.model import CommonMixin


class Topic(CommonMixin, db.Model):
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text)
    views = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    tab_id = db.Column(db.Integer, db.ForeignKey('tab.id'))
    replies = db.relationship('Reply', backref='topics', lazy='dynamic')

    def __repr__(self):
        return '<Topic {}>'.format(self.title)

    @classmethod
    def get(cls, id):
        t = cls.find_by(id=id)
        t.views += 1    # 点击数+1
        db.session.add(t)
        db.session.commit()
        return t

    def retries_true(self):
        from app.reply.model import Reply
        return Reply.query.filter_by(deleted=False, topic_id=self.id).all()