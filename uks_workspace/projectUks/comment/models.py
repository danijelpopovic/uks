from django.db import models
from issue.models import Issue
from django.conf import settings


class Comment(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1024)
    date_created = models.DateTimeField('date created')
    issue = models.ForeignKey(Issue, related_name='issue')
    author_comment = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, related_name='author_comment')
