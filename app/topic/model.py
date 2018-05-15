# coding: utf-8
from app import db
from app.common.model import CommonMixin


class Topic(CommonMixin, db.Model):
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return '<Topic {}>'.format(self.title)

