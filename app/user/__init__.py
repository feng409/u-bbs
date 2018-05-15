# coding: utf-8

from flask import Blueprint

bp = Blueprint('user', __name__)

from . import routes
