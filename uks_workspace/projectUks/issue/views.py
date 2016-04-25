from django.shortcuts import render
from .forms import IssueForm
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from repository.models import Repository
from repository.views import view_repository

# Create your views here.


def new_issue(request, repository_id):

    repository = get_object_or_404(Repository, id=repository_id)
    # title = request.POST.get("title")
    # description = request.POST.get("description")
    # date_created =
    # date_modified =
    # date_closed = None
    # is_closed = False
    # repository =
    # issue_author =
    # assigned = None
    form = IssueForm(request.POST)
    context = {
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.date_created = datetime.now
        instance.date_modified = datetime.now
        instance.date_closed = None
        instance.is_closed = False
        instance.repository = repository
        instance.issue_author = request.user
        instance.save()

        return view_repository(request, repository_id = repository_id)

    return render(request, "create_issue.html", context)
