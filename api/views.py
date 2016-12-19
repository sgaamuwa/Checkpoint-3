from api.models import Bucketlist, Item
from api.pagination import BucketlistListPagination
from api.permissions import IsOwner
from api.serializers import (
    BucketlistSerializer,
    BucketlistItemSerializer
)
from rest_framework import generics, exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class BucketlistList(generics.ListCreateAPIView):
    """View for Listing and Creation of Bucketlists
    in the database, requires authentication and ownership
    """
    serializer_class = BucketlistSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsOwner, IsAuthenticated,)
    pagination_class = BucketlistListPagination

    def get_queryset(self):
        # return only bucketlists for the given user
        user = self.request.user
        return Bucketlist.objects.filter(created_by=user.id)

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
    permission_classes = (IsOwner, IsAuthenticated,)


class BucketlistItemCreate(generics.CreateAPIView):
    """View for Creating Bucketlist Items,
    requires authentication and ownership of the specified bucketlist
    """
    serializer_class = BucketlistItemSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsOwner, IsAuthenticated,)

    def perform_create(self, serializer):
        # parse the bucketlist to which it belongs
        bucketlist_id = self.kwargs.get("pk")
        try:
            bucketlist = Bucketlist.objects.get(id=bucketlist_id)
        except:
            raise exceptions.NotFound()
        if bucketlist.created_by == self.request.user:
            serializer.save(bucketlist=bucketlist)
        else:
            raise exceptions.PermissionDenied(
                "You do not have permission to perform this action."
            )


class BucketlistItemDetail(generics.UpdateAPIView, generics.DestroyAPIView):
    """View for Updating and Deleting BucketlistItems in the database,
    Requires authentication and ownership of the item
    """
    queryset = Item.objects.all()
    serializer_class = BucketlistItemSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsOwner, IsAuthenticated,)
    lookup_field = ('id')

    def perform_update(self, serializer):
        # parse the bucketlist to which it belongs
        bucketlist_id = self.kwargs.get("pk")
        try:
            bucketlist = Bucketlist.objects.get(id=bucketlist_id)
        except:
            raise exceptions.NotFound()
        if bucketlist.created_by == self.request.user:
            serializer.save(bucketlist=bucketlist)
        else:
            raise exceptions.PermissionDenied(
                "You do not have permission to perform this action."
            )
