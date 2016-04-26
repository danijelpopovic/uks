from django.conf.urls import url
from django.contrib import admin
from .views import (
    base_index,
    logout_user,
    template_page,
    template2_page
)

urlpatterns = [
    url(r'^$', base_index, name='index'),
    url(r'^template/$', template_page, name='template_page'),
    url(r'^template2/$', template2_page, name='template2_page'),
]
