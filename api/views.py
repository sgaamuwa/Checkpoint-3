from api.models import Bucketlist, Item
from api.permissions import IsOwner
from api.serializers import (
    UserSerializer,
    BucketlistSerializer,
    BucketlistItemSerializer
)
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class UserCreate(generics.CreateAPIView):
    """View set for List, Get, Update, Delete and Create
    users in the database
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BucketlistList(generics.ListCreateAPIView):
    """View for Listing and Creation of Bucketlists
    in the database, requires authentication and ownership
    """
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        # pass the request user to the serializer
        serializer.save(created_by=self.request.user)


class BucketlistDetail(generics.RetrieveUpdateDestroyAPIView):
    """View for Get, Update and Deletion of Bucketlists
    in the database, requires authentication and ownership
    """
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsOwner)


class BucketlistItemCreate(generics.CreateAPIView):
    """View set for List, Get, Update, Delete and Create
    BucketlistItems in the database
    """
    queryset = Item.objects.all()
    serializer_class = BucketlistItemSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        # parse the bucketlist to which it belongs
        serializer.save()


class BucketlistItemDetail(generics.UpdateAPIView, generics.DestroyAPIView):
    """View set for List, Get, Update, Delete and Create
    BucketlistItems in the database
    """
    queryset = Item.objects.all()
    serializer_class = BucketlistItemSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsOwner)
