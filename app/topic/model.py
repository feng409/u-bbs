# coding: utf-8
from app import db
from app.common.model import CommonMixin


class Topic(CommonMixin, db.Model):
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text)
    views = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    tab_id = db.Column(db.Integer, db.ForeignKey('tab.id'))

    def __repr__(self):
        return '<Topic {}>'.format(self.title)

    @classmethod
    def get(cls, id):
        t = cls.find_by(id=id)
        t.views += 1    # 点击数+1
        db.session.add(t)
        db.session.commit()
        return t
