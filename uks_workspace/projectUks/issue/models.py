from django.db import models
from django.conf import settings

from repository.models import Repository

class Issue(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1024)
    date_created = models.DateTimeField('date created')
    date_modified = models.DateTimeField('date modified')
    date_closed = models.DateTimeField('date closed')
    is_closed = models.BooleanField
    repository = models.ForeignKey(Repository, related_name='repository')
    issue_author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, related_name='issue_author')
    assigned = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='assigned')
