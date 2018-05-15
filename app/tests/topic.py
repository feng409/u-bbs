# coding: utf-8
import unittest
from app.topic.model import Topic
from app.user.model import User
from app import create_app, db


class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class TopicModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_topic(self):
        user = User.new(
            username='u14e',
            password='123',
            email='123456@qq.com'
        )
        topic = Topic.new(
            user_id=user.id,
            title='开心呢',
            content="哈哈"
        )

        self.assertEqual(user.id, topic.user_id)


if __name__ == '__main__':
    unittest.main(verbosity=2)
