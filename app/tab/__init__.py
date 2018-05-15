# coding: utf-8

from flask import Blueprint

bp = Blueprint('tab', __name__)

from . import routes
