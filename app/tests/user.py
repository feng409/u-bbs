# coding: utf-8
import unittest
from app.user.model import User
from app import create_app, db


class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_register(self):
        user_email = dict(
            username='u14e',
            email='123',
            password='123'
        )
        u, result = User.register(user_email)
        print(u, result)
        self.assertFalse(u)

        user = dict(
            username='u14e',
            email='467030463@qq.com',
            password='123'
        )
        u, result = User.register(user)
        self.assertTrue(u)


if __name__ == '__main__':
    unittest.main(verbosity=2)
