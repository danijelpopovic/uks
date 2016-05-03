from django.shortcuts import render, render_to_response
from django.template import RequestContext

from comment.models import Comment
from issue.models import Issue
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
    repository = get_object_or_404(Repository, id=repository_id)
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

        return view_repository(request, repository_id=repository_id)

    return render(request, "create_issue.html", context)


def edit(request, repository_id, issue_id=None):
    if id:
        issue = get_object_or_404(Issue, id=issue_id)

        if request.POST:
            issue.repository = get_object_or_404(Repository, id=repository_id)
            form = IssueForm(request.POST, instance=issue)
            if form.is_valid():
                form.save()
                # If the save was successful, redirect to another page
                return view_repository(request, repository_id=repository_id)

        else:
            form = IssueForm(instance=issue)

    return render_to_response("issue_edit.html", {'form': form, }, context_instance=RequestContext(request))


def close_issue(request, issue_id, repository_id):
    issue = get_object_or_404(Issue, id=issue_id)
    value = False
    if issue.is_closed:
        value = False
    else:
        value = True

    Issue.objects.filter(id=issue_id).update(is_closed=value, date_closed=datetime.now())

    return view_repository(request, repository_id=repository_id)


def details(request, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)
    comments = Comment.objects.filter(issue=issue)
    context = {
        'issue': issue,
        'comments': comments,
    }
    return render(request, "issue_details.html", context)
