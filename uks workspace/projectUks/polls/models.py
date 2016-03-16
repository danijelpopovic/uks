from django.db import models

class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

class Repository(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    isPrivate = models.BooleanField
    contributions = models.ManyToManyField('User', related_name='contributions')
    author = models.ForeignKey(User, related_name='author')

class Issue(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1024)
    date_created = models.DateTimeField('date created')
    date_modified = models.DateTimeField('date modified')
    date_closed = models.DateTimeField('date closed')
    is_closed = models.BooleanField
    repository = models.ForeignKey(Repository, related_name='repository')
    issue_author = models.ForeignKey(User, related_name='issue_author')
    assigned = models.ManyToManyField('User', related_name='assigned')

class Comment(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1024)
    date_created = models.DateTimeField('date created')
    issue = models.ForeignKey(Issue, related_name='issue')
    author_comment = models.ForeignKey(User, related_name='author_comment')