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
from .model import User


@bp.route('/login', methods=['GET', 'POST'])
def login():
    pass


@bp.route('/logout')
def logout():
    pass


@bp.route('/register', methods=['GET', 'POST'])
def register():
    pass


