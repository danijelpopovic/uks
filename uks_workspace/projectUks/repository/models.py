from django.db import models
from django.conf import settings


class Repository(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    isPrivate = models.BooleanField
    contributions = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='contributions')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, related_name='author')
