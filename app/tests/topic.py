# coding: utf-8
import unittest
from app.topic.model import Topic
from app.user.model import User
from app.reply.model import Reply
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

    def user_recent_join_topics(self):
        """
        测试用户参与的话题，只包括评论过的
        :return:
        """
        user = User.new(
            username='u14e',
            password='123',
            email='123456@qq.com'
        )
        reply_user = User.new(
            username='other',
            password='123',
            email='123455@qq.com'
        )
        topic = Topic.new(
            user_id=user.id,
            title='开心呢',
            content="哈哈"
        )
        reply_topic = Topic.new(
            user_id=reply_user.id,
            title='回复的主题',
            content="噗噗噗"
        )
        reply = Reply.new(
            user_id=reply_user.id,
            content="评论1",
            topic_id=topic.id
        )

        self.assertIn(reply_user.recent_join_topics(), [topic]) # reply_user评论的主题
        self.assertNotIn(reply_user.recent_join_topics(), [reply_topic])    # reply_user创建的


if __name__ == '__main__':
    unittest.main(verbosity=2)
