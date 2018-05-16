# coding: utf-8
from flask import Blueprint

bp = Blueprint('message', __name__)

from . import routes