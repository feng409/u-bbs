# coding: utf-8

from flask import Blueprint

bp = Blueprint('topic', __name__)

from . import routes
