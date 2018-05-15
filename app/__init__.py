# coding: utf-8
import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask
from config import Config, base_dir
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.user import bp as user_bp
    app.register_blueprint(user_bp, url_prefix='/user')

    from app.topic import bp as topic_bp
    app.register_blueprint(topic_bp)

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
