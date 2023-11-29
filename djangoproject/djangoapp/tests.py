from django.test import TestCase
from .models import User


class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(telegram_id=123456, username='test_user')

    def test_user_creation(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_user_username(self):
        user = User.objects.get(telegram_id=123456)
        self.assertEqual(user.username, 'test_user')

    def test_user_instance(self):
        user = User.objects.get(telegram_id=123456)
        self.assertIsInstance(user, User)
