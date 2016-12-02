from api.models import Bucketlist, Item
from django.contrib import admin


class ItemField(admin.TabularInline):
    """Defines fields for adding items to a bucketlist"""
    model = Item
    extra = 2


class BucketlistAdmin(admin.ModelAdmin):
    """Defines fields for adding and listing bucketlists"""
    fields = ['name', 'created_by']
    inlines = [ItemField]
    list_display = ('name', 'date_created', 'date_modified', 'created_by')

admin.site.register(Bucketlist, BucketlistAdmin)

