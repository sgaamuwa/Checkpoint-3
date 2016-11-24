from api.models import Bucketlist, Item
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100, required=True)
    password = serializers.CharField(max_length=100, required=True)

    def validate_username(self, value):
        """Validate that the username is correct and unique"""
        if not value:
            raise serializers.ValidationError("Username required")
        elif len(value.strip()) < 4:
            raise serializers.ValidationError("Username is too short")
        elif value in [user.username for user in User.objects.all()]:
            raise serializers.ValidationError("Username already exists")
        return value

    def validate_password(self, value):
        """Validate that a proper password is passed"""
        if not value:
            raise serializers.ValidationError("Password required")
        elif len(value.strip()) < 4:
            raise serializers.ValidationError("Password is too short")
        return value

    class Meta:
        model = User
        fields = ("username", "password")


class BucketlistItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)

    def validate_name(self, value):
        """validation method for the name of the Bucketlist Item
        During both creation and updating
        """
        if not value:
            raise serializers.ValidationError("Please enter a name")
        elif len(value.strip()) < 2:
            raise serializers.ValidationError("Name is too short")
        return value

    class Meta:
        model = Item
        fields = "__all__"
        # it might be risky to do this
        validators = [
            UniqueTogetherValidator(
                queryset=Item.objects.all(),
                fields=("bucketlist", "name")
            )
        ]


class BucketlistSerializer(serializers.ModelSerializer):
    items = BucketlistItemSerializer(many=True, read_only=True)
    name = serializers.CharField(max_length=100)

    def validate_name(self, value):
        """validation method for the name of the Bucketlist
        During both creation and updating
        """
        if not value:
            raise serializers.ValidationError("Please enter a name")
        elif len(value.strip()) < 2:
            raise serializers.ValidationError("Name is too short")
        elif value in [blist.name for blist in Bucketlist.objects.all()]:
            raise serializers.ValidationError("Name already exists")
        return value

    class Meta:
        model = Bucketlist
        fields = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset=Bucketlist.objects.all(),
                fields=("created_by", "name")
            )
        ]
