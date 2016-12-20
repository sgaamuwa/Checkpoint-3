from django.db import models
from django.contrib.auth.models import User


class Bucketlist(models.Model):
    """Model for the bucketlist"""
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bucketlists"
    )
    # composite foreign key is the created by and bucketlist name columns

    class Meta:
        unique_together = ('created_by', 'name')

    def convert_date_created(self):
        return self.date_created.strftime("%a, %d %b %Y %H:%M:%S")

    def convert_date_modified(self):
        return self.date_modified.strftime("%a, %d %b %Y %H:%M:%S")

    def __str__(self):
        return self.name


class Item(models.Model):
    """Model for the item"""
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)
    bucketlist = models.ForeignKey(
        Bucketlist,
        on_delete=models.CASCADE,
        related_name="items"
    )
    # composite foreign key is the bucketlist and item name columns

    class Meta:
        unique_together = ('bucketlist', 'name')

    def convert_date_created(self):
        return self.date_created.strftime("%a, %d %b %Y %H:%M:%S")

    def convert_date_modified(self):
        return self.date_modified.strftime("%a, %d %b %Y %H:%M:%S")

    def __str__(self):
        return self.name
