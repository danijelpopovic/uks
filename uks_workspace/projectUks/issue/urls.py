from django.conf.urls import url

from .views import (
    new_issue,
)

urlpatterns = [

    url(r'^new/(?P<repository_id>\d+)/$', new_issue, name='new'),
]
