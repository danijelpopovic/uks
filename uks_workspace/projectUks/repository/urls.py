from django.conf.urls import url
from django.contrib import admin

from .views import (
	repository_list
	)

urlpatterns = [
	url(r'^$', repository_list, name='list')
]