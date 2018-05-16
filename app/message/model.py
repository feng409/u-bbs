# coding: utf-8
from app import db
from app.common.model import CommonMixin


class Message(CommonMixin, db.Model):
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Topic {}\nsender_id: {}\nreceiver_id: {}\n>'.format(self.title,
                                                                     self.sender_id,
                                                                     self.receiver_id)

