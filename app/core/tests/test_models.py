from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models

def sampleUser(email='test@slicelime.com',password='testpass'):
    """create a sample user"""
    return get_user_model().objects.create_user(email,password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@londonappdev.com'
        password = 'Password123'
        user = get_user_model().objects.create_user(
			email=email,
			password=password
		)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test is for new user is normalize"""
        email = 'test@SLICELIME.com'
        user = get_user_model().objects.create_user(email,'test123')

        self.assertEqual(user.email,email.lower())

    def test_new_user_invlaid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test123')

    def test_create_superuser(self):
        """Test Creating a new superuser"""

        user = get_user_model().objects.create_superuser(
            'test@slicelime.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test tag string rep"""
        tag = models.Tag.objects.create(
            user = sampleUser(),
            name = 'Vegan'
        )
        self.assertEqual(str(tag),tag.name)