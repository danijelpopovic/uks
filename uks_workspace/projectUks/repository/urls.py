from django.conf.urls import url
from django.contrib import admin

from .views import (
	repository_list,
	new_repository)

urlpatterns = [
	url(r'^$', repository_list, name='list'),
	url(r'^new/', new_repository,name='new'),
]