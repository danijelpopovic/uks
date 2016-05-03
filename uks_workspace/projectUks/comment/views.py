from datetime import datetime
from django.shortcuts import render, get_object_or_404

from comment.forms import CommentForm
from comment.models import Comment
from issue.models import Issue


def new_comment(request, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)
    form = CommentForm(request.POST)

    context = {
        "form": form,
        "issue": issue,
        "comments": Comment.objects.filter(issue=issue)
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.date_created = datetime.now
        instance.issue = issue
        instance.author_comment = request.user
        instance.save()

        return render(request, "comment_list.html", context)

    return render(request, "comment_new.html", context)
