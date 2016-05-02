"""projectUks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView





urlpatterns = {

    url(r'^login/$', 'base.views.login_user'),
    url(r'^logout/$', 'base.views.logout_user'),
    url('^register/', CreateView.as_view(
        template_name='register.html',
        form_class=UserCreationForm,
        success_url='/'
    )),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^repository/', include("repository.urls", namespace='repository')),
    url(r'^issue/', include("issue.urls", namespace='issue')),
    url(r'^', include("base.urls", namespace='base')),
}
