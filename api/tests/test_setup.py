from django.contrib.auth.models import User
from api.models import Bucketlist, Item
from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token


class BaseTestCase(APITestCase):
    """Base test class for all tests for the APIClient
    Sets up test users, bucketlists and bucketlist items
    """
    def setUp(self):
        # set the clients for the tests in
        self.client = APIClient()
        self.client_2 = APIClient()
        # add two users to the system
        self.user_1 = User.objects.create(
            username="samuel",
            password="pass123"
        )
        self.user_2 = User.objects.create(
            username="marvin",
            password="pass123"
        )
        # login in the users
        self.client.login(username='samuel', password='pass123')
        self.client_2.login(username='marvin', password='pass123')
        # get tokens for the two users
        token_1 = Token.objects.get_or_create(user=self.user_1)
        token_2 = Token.objects.get_or_create(user=self.user_2)
        # set the authentication for the clients
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token_1[0].key)
        self.client_2.credentials(HTTP_AUTHORIZATION='Token ' + token_2[0].key)
        # create bucketlists belonging to both
        self.bucketlist_1 = Bucketlist.objects.create(
            name="test_bucketlist_1",
            created_by=self.user_1
        )
        # bucketlist for the second user
        self.bucketlist_2 = Bucketlist.objects.create(
            name="test_bucketlist_2",
            created_by=self.user_2
        )
        # create test items
        Item.objects.create(
            name="test_item_1",
            done=False,
            bucketlist=self.bucketlist_1,
        )
        # item belonging to second bucketlist and user
        Item.objects.create(
            name="test_item_2",
            done=False,
            bucketlist=self.bucketlist_2,
        )
