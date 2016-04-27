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
    request.session['menu'] = 'home'
    if request.user.is_authenticated():
        return render(request, 'index.html', context_instance=RequestContext(request))
    else:
        return render(request, 'login.html', context_instance=RequestContext(request))


def template_page(request):
    return render(request, 'template.html', context_instance=RequestContext(request))


def template2_page(request):
    return render(request, 'templateForm.html', context_instance=RequestContext(request))
# def register(request):
#     if request.method == 'POST':
#         uf = UserForm(request.POST, prefix='user')
#         upf = UserProfileForm(request.POST, prefix='userprofile')
#         if uf.is_valid() * upf.is_valid():
#             user = uf.save()
#             userprofile = upf.save(commit=False)
#             userprofile.user = user
#             userprofile.save()
#             return HttpResponseRedirect('/')
#     else:
#         uf = UserForm(prefix='user')
#         upf = UserProfileForm(prefix='userprofile')
#     return render_to_response('register_user.html',
#                                                dict(userform=uf,
#                                                     userprofileform=upf),
#                                                context_instance=RequestContext(request))
