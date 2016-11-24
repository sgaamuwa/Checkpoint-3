from api.models import Bucketlist, Item
from api.serializers import UserSerializer, BucketlistSerializer,
BucketlistItemSerializer
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets


class UserViewSet(viewsets.ViewSet):
    """View set for List, Get, Update, Delete and Create 
    users in the database
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BucketlistViewSet(viewsets.ViewSet):
    """View set for List, Get, Update, Delete and Create 
    Bucketlists in the database
    """
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    authentication_classes = (TokenAuthentication)
    permission_classes = []


class BucketlistItemViewSet(viewsets.ViewSet):
    """View set for List, Get, Update, Delete and Create 
    BucketlistItems in the database
    """
    queryset = Item.objects.all()
    serializer_class = BucketlistItemSerializer
    permission_classes = []