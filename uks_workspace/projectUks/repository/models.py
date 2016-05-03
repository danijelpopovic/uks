import datetime
from django.db import models
from django.conf import settings


class RepositoryManager(models.Manager):
    def active(self, user, *args, **kwargs):
        result = super(RepositoryManager, self).filter(author=user.id)

        return result


class Repository(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    isPrivate = models.BooleanField(default=True)
    contributions = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='contributions')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, related_name='author')

    objects = RepositoryManager()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_contributions(self):
        return "\n".join([p.contributions for p in self.contributions.all()])
