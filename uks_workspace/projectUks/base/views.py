from django.shortcuts import render
from repository.models import Repository
from django.http import *
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from .models import *
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    return render(request, 'login.html', context_instance=RequestContext(request))


def logout_user(request):
    if request.user is not None:
        logout(request)
    return render(request, 'login.html', context_instance=RequestContext(request))


def base_index(request):
    if request.user.is_authenticated():
        return render(request, 'index.html', context_instance=RequestContext(request))
    else:
        return render(request, 'login.html', context_instance=RequestContext(request))
