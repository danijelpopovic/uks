from django.db import models
from django.conf import settings



# class User(models.Model):
#     email = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     username = models.CharField(max_length=100)

# class Repository(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.CharField(max_length=100)
#     isPrivate = models.BooleanField
#     contributions = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='contributions')
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, related_name='author')


# class Issue(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.CharField(max_length=1024)
#     date_created = models.DateTimeField('date created')
#     date_modified = models.DateTimeField('date modified')
#     date_closed = models.DateTimeField('date closed')
#     is_closed = models.BooleanField
#     repository = models.ForeignKey(Repository, related_name='repository')
#     issue_author = models.ForeignKey(User, related_name='issue_author')
#     assigned = models.ManyToManyField('User', related_name='assigned')

# class Comment(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.CharField(max_length=1024)
#     date_created = models.DateTimeField('date created')
#     issue = models.ForeignKey(Issue, related_name='issue')
#     author_comment = models.ForeignKey(User, related_name='author_comment')

# class Object(models.Model):
#     date_created = models.DateTimeField('date created')
#
# class Folder(Object):
#      name = models.CharField(max_length=100)
#      repository_folder = models.ForeignKey(Repository, related_name='repository_folder')
#      subfolder = models.ForeignKey('self')
#
# class File(Object):
#     name = models.CharField(max_length=100)
#     size = models.IntegerField(default=0)
#     folder_obj = models.ForeignKey(Folder, related_name='folder_obj')

# class Version(models.Model):
#      date = models.DateTimeField('date')
#      object_version = models.ManyToManyField(Object, related_name='object_version')
#      user_version = models.ForeignKey(User, related_name='user_version')
