from django.conf.urls import url
from django.contrib import admin
from .views import (
    repository_list,
    new_repository,
    edit,
    view_repository)

urlpatterns = [
    url(r'^$', repository_list, name='list'),
    url(r'^new/', new_repository, name='new'),
    url(r'^edit/(?P<repository_id>\d+)/$', edit, name='edit'),
    url(r'^view/(?P<repository_id>[0-9]+)/$', view_repository, name='view'),

]
