from django.conf.urls import url
from api.views import (
    BucketlistDetail,
    BucketlistItemCreate,
    BucketlistItemDetail,
    BucketlistList,
    )
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^bucketlists/$', BucketlistList.as_view()),
    url(
        r'^bucketlists/(?P<pk>[0-9]+)/items/$',
        BucketlistItemCreate.as_view()
    ),
    url(
        r'^bucketlists/(?P<pk>[0-9]+)/items/(?P<pk2>[0-9]+)',
        BucketlistItemDetail.as_view()
    ),
    url(r'^bucketlists/(?P<pk>[0-9]+)', BucketlistDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
