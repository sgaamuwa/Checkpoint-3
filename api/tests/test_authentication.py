from api.tests import test_setup
from django.contrib.auth.models import User
from rest_framework import status


class TestAuthentication(test_setup.BaseTestCase):
    """Class for testing all authentication endpoints and test cases
    That is for registration and login of users
    """

    def test_register_user(self):
        """test that a user is created and added to the database"""
        self.assertEqual(User.objects.count(), 2)
        response = self.client.post(
            "/api/auth/register/",
            {"username": "monreal", "password": "pass123"},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 3)

    def test_register_existent_user(self):
        """test cant register a user that already exists"""
        self.assertEqual(User.objects.count(), 2)
        response = self.client.post(
            "/api/auth/register/",
            {"username": "samuel", "password": "pass123"},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            {'username': ['A user with that username already exists.']},
            response.data
        )
        self.assertEqual(User.objects.count(), 2)

    def test_register_user_no_data(self):
        response = self.client.post(
            "/api/auth/register/",
            {"username": "", "password": ""},
            format="json"
        )
        self.assertEqual(
            {
                'password': ['This field may not be blank.'],
                'username': ['This field may not be blank.']
            },
            response.data
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_user(self):
        """test that a created user can log into the system"""
        # login the user
        response = self.client.post(
            "/api/auth/login/",
            {"username": "samuel", "password": "pass123"},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_unregistered_user(self):
        """test that cant login unregistered users"""
        response = self.client.post(
            "/api/auth/login/",
            {'username': 'monreal', 'password': 'pass123'},
            format="json"
        )
        self.assertEqual(
            ['Unable to login with provided credentials.'],
            response.data["non_field_errors"]
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_with_bad_data(self):
        """test cant login without correct credentials"""
        response = self.client.post(
            "/api/auth/login/",
            {"username": "samuel", "password": "pass"},
            format="json"
        )
        self.assertEqual(
            ['Unable to login with provided credentials.'],
            response.data["non_field_errors"]
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # test login without data
        response = self.client.post(
            "/api/auth/login/",
            {"username": "", "password": ""},
            format="json"
        )
        self.assertEqual(
            {
                'password': ['This field may not be blank.'],
                'username': ['This field may not be blank.']
            },
            response.data
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
