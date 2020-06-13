from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'test@gmail.com'
        password = 'pass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertEqual(user.check_password(password), True)

    def test_new_user_email_normalized(self):
        email = 'test@EMAIL.COM'
        user = get_user_model().objects.create_user(email, 'pass1234')

        self.assertEqual(user.email, email.lower())
    
    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'pass123')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'testpass1234'
        )
        
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)