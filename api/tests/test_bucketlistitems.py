from api.models import Item
from rest_framework import status
from api.tests import test_setup


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
        self.assertEqual(
            {'name': ['This field may not be blank.']},
            response.data
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_bucketlistitem_unauthorized(self):
        """test cant create bucketlistitem without Authentication"""
        self.client.credentials()
        response = self.client.post(
            "/bucketlists/1/items/",
            {"name": "new_item"},
            format="json"
        )
        self.assertEqual(
            {'detail': 'Authentication credentials were not provided.'},
            response.data
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_bucketlistitem_not_owner(self):
        """test cant create a bucketlist item if not owner of bucketlist"""
        response = self.client_2.post(
            "/bucketlists/1/items/",
            {"name": "new_item"},
            format="json"
        )
        self.assertEqual(
            {'detail': 'You do not have permission to perform this action.'},
            response.data
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_bucketlistitem_for_non_existent_bucketlist(self):
        """test cant create item if bucketlist does not exist"""
        response = self.client.post(
            "/bucketlists/11/items/",
            {"name": "new_item"},
            format="json"
        )
        self.assertEqual({'detail': 'Not found.'}, response.data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_bucketlistitem_with_short_name(self):
        """test cant create item with a name less than 2 characters"""
        response = self.client.post(
            "/bucketlists/1/items/",
            {"name": "d"},
            format="json"
        )
        self.assertEqual(
            {'name': ['Name is too short']},
            response.data
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_bucketlistitem(self):
        """test that a bucketlist item can be updated"""
        response = self.client.put(
            "/bucketlists/1/items/1",
            {"name": "new_item"},
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # test updating done status
        response = self.client.patch(
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
        self.assertEqual(
            {'detail': 'You do not have permission to perform this action.'},
            response.data
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_bucketlistitem_non_existent_bucketlist(self):
        """test cant update item if bucketlist does not exist"""
        response = self.client.put(
            "/bucketlists/11/items/1",
            {"name": "new_item"},
            format="json"
        )
        self.assertEqual({'detail': 'Not found.'}, response.data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_bucketlistitem_not_owner(self):
        """test cant update a bucketlist item if not owner"""
        response = self.client_2.put(
            "/bucketlists/1/items/1",
            {"name": "new_item"},
            format="json"
        )
        self.assertEqual(
            {'detail': 'You do not have permission to perform this action.'},
            response.data
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_bucketlistitem_unauthorized(self):
        """test cant update a bucketlist item if not authentication"""
        self.client.credentials()
        response = self.client.put(
            "/bucketlists/1/items/1",
            {"name": "new_item"},
            format="json"
        )
        self.assertEqual(
            {'detail': 'Authentication credentials were not provided.'},
            response.data
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_bucketlistitem_with_no_data(self):
        """test cant udpate without data"""
        response = self.client.put(
            "/bucketlists/1/items/1",
            {"name": ""},
            format="json"
        )
        self.assertEqual(
            {'name': ['This field may not be blank.']},
            response.data
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # test updating done status
        response = self.client.patch(
            "/bucketlists/1/items/1",
            {"done": ""},
            format="json"
        )
        self.assertEqual(
            {'done': ['"" is not a valid boolean.']},
            response.data
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

    def test_delete_bucketlistitem_unauthorized(self):
        """test that cant delete bucketlistitem if not authenticated"""
        self.client.credentials()
        self.assertEqual(Item.objects.count(), 2)
        response = self.client.delete(
            "/bucketlists/1/items/1"
        )
        self.assertEqual(
            {'detail': 'Authentication credentials were not provided.'},
            response.data
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Item.objects.count(), 2)

    def test_delete_bucketlistitem_not_owner(self):
        """test cant delete bucketlistitem if not owner"""
        self.assertEqual(Item.objects.count(), 2)
        response = self.client_2.delete(
            "/bucketlists/1/items/1"
        )
        self.assertEqual(
            {'detail': 'You do not have permission to perform this action.'},
            response.data
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Item.objects.count(), 2)
