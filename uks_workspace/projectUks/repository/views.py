
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

from repository.models import Repository
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from forms import RepositoryForm


def repository_list(request):
    today = timezone.now().date()
    queryset_list = Repository.objects.active(request.user)

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
                Q(title__icontains=query)|
                Q(content__icontains=query)|
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
                ).distinct()
    paginator = Paginator(queryset_list, 8) # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)


    context = {
        "object_list": queryset,
        "title": "List",
        "page_request_var": page_request_var,
        "today": today,
    }
    return render(request, "repository_list.html", context)

def new_repository(request):
    name = request.POST.get("name")
    description = request.POST.get("description")
    is_private = request.POST.get("isPrivate")

    print(name)
    print(description)
    print(is_private)

    form = RepositoryForm(request.POST)
    context = {
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        return repository_list(request)



    return render(request, "create_repository.html", context)
