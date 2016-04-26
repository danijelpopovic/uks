from django.conf.urls import url

from .views import (
    new_issue,
    edit,
    details,
    close_issue
)

urlpatterns = [


    url(r'^new/(?P<repository_id>\d+)/$', new_issue, name='new'),
    url(r'^edit/(?P<repository_id>(\d+))/(?P<issue_id>\d+)/$', edit, name='edit'),
    url(r'^details/(?P<issue_id>\d+)/$', details, name='details'),
    url(r'^close/(?P<issue_id>(\d+))/(?P<repository_id>\d+)/$', close_issue, name='close'),
]
