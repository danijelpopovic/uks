import datetime
from django.db import models
from django.conf import settings


class RepositoryManager(models.Manager):
    def active(self, user, *args, **kwargs):
        # Post.objects.all() = super(PostManager, self).all()
        print("------------")
        result = super(RepositoryManager, self).filter(author=user.id)
        # repositories = Repository.objects.all()
        # list_rep = []
        # for r in repositories:
        #     for con in r.contributions.all():
        #         print(con.username)
        #         list_rep.append(r)
        #
        # result.extend(list(list_rep))
        # print(result)
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
