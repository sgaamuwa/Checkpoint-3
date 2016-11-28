from django.contrib.auth.models import User
from api.models import Bucketlist, Item
from rest_framework import status
from api.tests import test_setup


class TestAuthentication(test_setup.BaseTestCase):
    """Class for testing all authentication endpoints and test cases
    That is for registration and login of users
    """

    def test_register_user(self):
        """test that a user is created and added to the database"""
        self.assertEqual(User.objects.count(), 2)
        response = self.client.post(
            "/auth/register",
            {"username": "monreal", "password": "pass123"},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 3)

    def test_register_existent_user(self):
        """test cant register a user that already exists"""
        self.assertEqual(User.objects.count(), 2)
        response = self.client.post(
            "/auth/register",
            {"username": "samuel", "password": "pass123"},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            {'username': ['Username already exists']},
            response.data
        )
        self.assertEqual(User.objects.count(), 2)

    def test_register_user_no_data(self):
        response = self.client.post(
            "/auth/register",
            {"username": "", "password": ""},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_user(self):
        """test that a created user can log into the system"""
        # login the user
        response = self.client.post(
            "/auth/login",
            {"username": "samuel", "password": "pass123"},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_unregistered_user(self):
        """test that cant login unregistered users"""
        response = self.client.post(
            "/auth/login",
            {'username': 'monreal', 'password': 'pass123'},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_with_bad_data(self):
        """test cant login without correct credentials"""
        response = self.client.post(
            "/auth/login",
            {"username": "samuel", "password": "pass"},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # test login without data
        response = self.client.post(
            "/auth/login",
            {"username": "", "password": ""},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestBucketlists(test_setup.BaseTestCase):
    """Class for testing all bucketlist endpoints in the System
    That is creating, updating, listing, getting and deleting buckelists
    """

    def test_create_bucketlist(self):
        """test that a bucketlist can be created and added to the database"""
        self.assertEqual(Bucketlist.objects.count(), 2)
        response = self.client.post(
            "/bucketlists/",
            {"name": "new_bucketlist"},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bucketlist.objects.count(), 3)

    def test_create_bucketlist_unauthorized(self):
        """test cant create bucketlist without authorization"""
        self.client.credentials()
        response = self.client.post(
            "/bucketlists/",
            {"name": "new_bucketlist"},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_bucketlist_empty_name(self):
        """test cant create bucketlist without a name"""
        response = self.client.post(
            "/bucketlists/",
            {"name": ""},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_bucketlists(self):
        """test that bucketlists in the database can be retrieved"""
        response = self.client.get("/bucketlists/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_bucketlists_unauthorized(self):
        """test cant retrieve bucketlists if unauthorized"""
        self.client.credentials()
        response = self.client.get("/bucketlists/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_bucketlist(self):
        """test that a singular database can be retrieved"""
        response = self.client.get("/bucketlists/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_bucketlist_unauthorized(self):
        """test cant get a singular database if unauthorized"""
        self.client.credentials()
        response = self.client.get("/bucketlists/1")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_bucketlist(self):
        """test that a bucketlist in the database can be updated"""
        response = self.client.put(
            "/bucketlists/1",
            {"name": "new_bucketlist"},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_bucketlist_unauthorized(self):
        """test cant update a bucketlist if unauthorized"""
        self.client.credentials()
        response = self.client.put(
            "/bucketlists/1",
            {"name": "new_bucketlist"},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_bucketlist_with_no_data(self):
        """test that a bucketlist in the database can be updated"""
        response = self.client.put(
            "/bucketlists/1",
            {"name": ""},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_bucketlist(self):
        """test that a bucketlist can be deleted from the database"""
        self.assertEqual(Bucketlist.objects.count(), 2)
        response = self.client.delete(
            "/bucketlists/1"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Bucketlist.objects.count(), 1)

    def test_delete_bucketlist_unauthorized(self):
        """test cant delete a bucketlist if unauthorized"""
        self.client.credentials()
        response = self.client.delete(
            "/bucketlists/1"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_bucketlist_not_owner(self):
        """test cant delete bucketlist if not owner"""
        response = self.client_2.delete(
            "/bucketlists/1"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestBucketlistItems(test_setup.BaseTestCase):
    """Class for testing all bucketlist item endpoints in the api
    That is creating, updating and deleting
    """

    def test_create_bucketlistitem(self):
        """test that item can be created"""
        self.assertEqual(Item.objects.count(), 2)
        response = self.client.post(
            "/bucketlists/1/items/",
            {"name": "new_item"},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 3)

    def test_create_bucketlistitem_with_bad_data(self):
        """test cant create bucketlistitem without a name"""
        response = self.client.post(
            "/bucketlists/1/items/",
            {"name": ""},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_bucketlistitem_unauthorized(self):
        """test cant create bucketlistitem without a name"""
        self.client.credentials()
        response = self.client.post(
            "/bucketlists/1/items/",
            {"name": "new_item"},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_bucketlistitem_not_owner(self):
        """test cant create a bucketlist item if not owner of bucketlist"""
        response = self.client_2.post(
            "/bucketlists/1/items/",
            {"name": "new_item"},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_bucketlistitem_for_non_existent_bucketlist(self):
        """test cant create item if bucketlist does not exist"""
        response = self.client.post(
            "/bucketlists/11/items/",
            {"name": "new_item"},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_bucketlistitem(self):
        """test that a bucketlist item can be updated"""
        response = self.client.put(
            "/bucketlists/1/items/1",
            {"name": "new_item"},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # test updating done status
        response = self.client.put(
            "/bucketlists/1/items/1",
            {"done": True},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_bucketlistitem_wrong_bucketlist(self):
        """test cant update a bucketlistitem if bucketlist is wrong"""
        response = self.client.put(
            "/bucketlists/2/items/1",
            {"name": "new_item"},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_bucketlistitem_not_owner(self):
        """test cant update a bucketlist item if not owner"""
        response = self.client_2.put(
            "/bucketlists/1/items/1",
            {"name": "new_item"},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_bucketlistitem_unauthorized(self):
        """test cant update a bucketlist item if not authentication"""
        self.client.credentials()
        response = self.client.put(
            "/bucketlists/1/items/1",
            {"name": "new_item"},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_bucketlistitem_with_no_data(self):
        """test cant udpate without data"""
        response = self.client.put(
            "/bucketlists/1/items/1",
            {"name": ""},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # test updating done status
        response = self.client.put(
            "/bucketlists/1/items/",
            {"done": ""},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_bucketlistitem(self):
        """test that an item can be deleted"""
        self.assertEqual(Item.objects.count(), 2)
        response = self.client.delete(
            "/bucketlists/1/items/1"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Item.objects.count(), 1)
