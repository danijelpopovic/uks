from django.conf.urls import url
from django.contrib import admin
from .views import (
    base_index,
    logout_user
)

urlpatterns = [
    url(r'^$', base_index, name='index'),

]
