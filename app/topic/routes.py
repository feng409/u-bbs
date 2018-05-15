# coding: utf-8
from flask import (
    render_template,
    flash,
    redirect,
    url_for,
    request
)
from app import db
from . import bp
from app.user.model import User


@bp.route('/')
def index():
    return render_template('index.html', name="u14e")



