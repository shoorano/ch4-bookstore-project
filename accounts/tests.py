# accounts/tests.py
from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    def test_create_user(self):
        """test creation of user"""
        username = "dan"
        email = "dan@email.com"
        password = "testpass123"

        User = get_user_model()
        user = User.objects.create_user(username=username, email=email, password=password)
        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """test creation of superuser"""
        username = "superuser"
        email = "admin@email.com"
        password = "testpass123"

        User = get_user_model()
        user = User.objects.create_superuser(username=username, email=email, password=password)
        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
