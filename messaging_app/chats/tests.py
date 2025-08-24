import pytest
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

User = get_user_model()

class TestUserModel(TestCase):
    """Test cases for User model"""
    
    def test_create_user(self):
        """Test creating a new user"""
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpass123'))

    def test_user_str_representation(self):
        """Test the string representation of user"""
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com'
        )
        self.assertEqual(str(user), 'testuser')

class TestAPI(APITestCase):
    """Test cases for API endpoints"""
    
    def setUp(self):
        """Set up test data"""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    def test_user_list_unauthorized(self):
        """Test accessing user list without authentication"""
        # This test will depend on your actual API endpoints
        # Adjust the URL pattern based on your urls.py
        pass

@pytest.mark.django_db
class TestPytestIntegration:
    """Test cases using pytest syntax"""
    
    def test_pytest_user_creation(self):
        """Test user creation using pytest"""
        user = User.objects.create_user(
            username='pytestuser',
            email='pytest@example.com',
            password='testpass123'
        )
        assert user.username == 'pytestuser'
        assert user.email == 'pytest@example.com'
