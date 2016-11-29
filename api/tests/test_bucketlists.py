from api.models import Bucketlist
from rest_framework import status
from api.tests import test_setup


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
        self.assertEqual(
            {'detail': 'Authentication credentials were not provided.'},
            response.data
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
        self.assertEqual(
            {'detail': 'You do not have permission to perform this action.'},
            response.data
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
