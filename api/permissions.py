from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Object-level permission to only allow only owners to
    Interact with an object, that is view, edit and create
    """

    def has_object_permissions(self, request, view, obj):
        # return true if user is the owner of bucketlist
        return obj.created_by == request.user
