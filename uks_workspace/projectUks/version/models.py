from django.db import models
from django.conf import settings
from object.models import Object

class Version(models.Model):
     date = models.DateTimeField('date')
     object_version = models.ManyToManyField(Object, related_name='object_version')
     user_version = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, related_name='user_version')
