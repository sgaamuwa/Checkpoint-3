from api.models import Bucketlist, Item
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")


class BucketlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucketlist
        validators = [
            UniqueTogetherValidator(
                queryset=Bucketlist.objects.all(),
                fields=("created_by", "name")
            )
        ]


class BucketlistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        validators = [
            UniqueTogetherValidator(
                queryset=Item.objects.all(),
                fields=("bucketlist", "name")
            )
        ]
