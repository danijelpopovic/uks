import django.db
from django.conf import settings

from issue.models import Issue


class Comment(django.db.models.Model):
    title = django.db.models.CharField(max_length=100)
    content = django.db.models.CharField(max_length=1024)
    date_created = django.db.models.DateTimeField('date created')
    issue = django.db.models.ForeignKey(Issue, related_name='issue')
    author_comment = django.db.models.ForeignKey(settings.AUTH_USER_MODEL, default=1, related_name='author_comment')
