from django.db import models

from repository.models import Repository


class Object(models.Model):
    date_created = models.DateTimeField('date created')

class Folder(Object):
     name = models.CharField(max_length=100)
     repository_folder = models.ForeignKey(Repository, related_name='repository_folder')
     subfolder = models.ForeignKey('self', null=True, blank=True, default=None)

class File(Object):
    name = models.CharField(max_length=100)
    size = models.IntegerField(default=0)
    folder_obj = models.ForeignKey(Folder, related_name='folder_obj')
