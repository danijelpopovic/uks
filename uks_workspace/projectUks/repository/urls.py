from django.conf.urls import url
from django.contrib import admin
from .views import (
    repository_list,
    new_repository,
    view_repository)

urlpatterns = [
    url(r'^$', repository_list, name='list'),
    url(r'^new/', new_repository, name='new'),
    url(r'^(?P<repository_id>[0-9]+)/view/', view_repository, name='view'),

]
