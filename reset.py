# coding: utf-8
from app import create_app, db
from sqlalchemy import create_engine
from config import Config
from app.utils import log


def create_database(app):
    """
    创建或重置数据库
    """
    url = 'mysql+pymysql://root:admin@localhost/?charset=utf8mb4'
    log('数据库创建url:', url)
    e = create_engine(url, echo=True)

    with e.connect() as c:
        c.execute('DROP DATABASE IF EXISTS u_bbs')
        c.execute('CREATE DATABASE u_bbs CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci')
        c.execute('USE u_bbs')
    log('数据库创建完成')

    with app.app_context():
        db.create_all()
    log('表创建完成')


def run():
    app = create_app()
    create_database(app)


if __name__ == '__main__':
    run()
