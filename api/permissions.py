from api.models import Bucketlist, Item
from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow only owners to
    Interact with an object, that is view, edit and create
    """

    def has_object_permission(self, request, view, obj):
        # return true if user is the owner of bucketlist
        if type(obj) is Bucketlist:
            return obj.created_by == request.user
        elif type(obj) is Item:
            return obj.bucketlist.created_by == request.user
