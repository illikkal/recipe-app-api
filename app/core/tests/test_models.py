"""
Test database models 
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models"""
    def test_create_user_with_email_successfull(self):
        email = "test@example.com"
        password = "test123"
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users"""
        sample_emails = [
            ["test@EXAMPLE.COM", "test@example.com"]
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'test123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that user create without email raises value error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        """test create super user"""
        user = get_user_model().objects.create_superuser('adm@nmt.com', 'test123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)