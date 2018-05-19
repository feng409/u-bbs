# coding: utf-8
import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask, g, request
from config import Config, base_dir
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.utils import log, moment


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    # flask实例化
    app = Flask(__name__)
    # 配置
    app.config.from_object(config_class)

    # 插件
    db.init_app(app)
    migrate.init_app(app, db)

    # 蓝图
    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.user import bp as user_bp
    app.register_blueprint(user_bp, url_prefix='/user')

    from app.topic import bp as topic_bp
    app.register_blueprint(topic_bp)

    from app.tab import bp as tab_bp
    app.register_blueprint(tab_bp)

    from app.reply import bp as reply_bp
    app.register_blueprint(reply_bp)

    from app.message import bp as message_bp
    app.register_blueprint(message_bp, url_prefix='/message')

    from app.common import current_user

    # 添加过滤器
    app.add_template_filter(moment)

    @app.before_request
    def app_before_req():
        # 每次请求获取当前用户，设置全局变量
        g.user = current_user()
        # log('='*20)
        # log('remote address and user:', request.remote_addr, request.remote_user)
        # log('x-real-ip:', request.headers['x-real-ip'])
        # log('x-forwarded-for:', request.headers['x-forwarded-for'])
        # log('=' * 20)
        log('before_request current_user:', g.user)

    # debug模式和测试环境下不要开启
    if not app.debug and not app.testing:
        # 将日志存到本地文件
        log_dir = os.path.join(base_dir, 'logs')
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
        log_file = os.path.join(log_dir, 'u-bbs.log')
        file_handler = RotatingFileHandler(log_file,
                                           maxBytes=10240,
                                           backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('u-bbs startup')

    return app


from app.user.model import User
from app.topic.model import Topic
from app.tab.model import Tab
from app.reply.model import Reply
from app.message.model import Message
