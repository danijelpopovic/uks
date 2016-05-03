from django.conf.urls import url

from .views import (
    new_comment
)

urlpatterns = [
    url(r'^new/(?P<issue_id>\d+)', new_comment, name='new'),
]
