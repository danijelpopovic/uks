from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from .models import *
from django.utils import timezone
from .forms import RepositoryForm
from issue.models import Issue


def repository_list(request):
    today = timezone.now().date()
    queryset_list = Repository.objects.active(request.user)

    request.session['menu'] = 'repository'

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        ).distinct()

    paginator = Paginator(queryset_list, 8)
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

    repositories = Repository.objects.all()

    res = []
    repositoriesuser = repositories.filter(author=request.user.id)
    if repositoriesuser != None:
        for repos in repositoriesuser:
            res.append(repos)

    for r in repositories:
        for con in r.contributions.all():
            if con == request.user and r not in res:
                res.append(r)

    context = {
        "object_list": res,
        "title": "List",
        "page_request_var": page_request_var,
        "today": today,
    }
    return render(request, "repository_list.html", context)


def new_repository(request):
    request.session['menu'] = 'repository'
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


def edit(request, repository_id=None):
    request.session['menu'] = 'repository'
    if id:
        repository = get_object_or_404(Repository, id=repository_id)

        if request.POST:
            form = RepositoryForm(request.POST, instance=repository)
            if form.is_valid():
                form.save()
                return repository_list(request)

        else:
            form = RepositoryForm(instance=repository)

    return render_to_response("repository_edit.html", {'form': form, }, context_instance=RequestContext(request))


def view_repository(request, repository_id):
    request.session['menu'] = 'repository'
    repository = get_object_or_404(Repository, pk=repository_id)
    issues = Issue.objects.filter(repository=repository)
    context = {

        'repository': repository,
        'issues': issues
    }
    return render(request, "repository.html", context)
