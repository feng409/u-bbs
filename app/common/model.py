# coding: utf-8
from app import db
import time


class CommonMixin:
    id = db.Column(db.Integer, primary_key=True)
    deleted = db.Column(db.Boolean, nullable=False, default=False)
    created_time = db.Column(db.Integer, default=time.time)
    updated_time = db.Column(db.Integer, onupdate=True, default=time.time)

    @classmethod
    def exist(cls, **kwargs):
        first = cls.query.filter_by(**kwargs).first()
        return first
