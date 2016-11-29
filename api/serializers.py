from api.models import Bucketlist, Item
from rest_framework import serializers


class BucketlistItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    done = serializers.BooleanField(default=False)

    def validate_name(self, value):
        """validation method for the name of the Bucketlist Item
        During both creation and updating
        """
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Name is too short")
        return value

    class Meta:
        model = Item
        fields = ("id", "name", "date_created", "date_modified", "done")


class BucketlistSerializer(serializers.ModelSerializer):
    items = BucketlistItemSerializer(many=True, read_only=True)
    name = serializers.CharField(max_length=100)
    created_by = serializers.ReadOnlyField(source='created_by.id')

    def validate_name(self, value):
        """validation method for the name of the Bucketlist
        During both creation and updating
        """
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Name is too short")
        elif value in [blist.name for blist in Bucketlist.objects.all()]:
            raise serializers.ValidationError("Name already exists")
        return value

    class Meta:
        model = Bucketlist
        fields = "__all__"
