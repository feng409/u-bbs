# coding: utf-8

from flask import Blueprint

bp = Blueprint('reply', __name__)

from . import routes