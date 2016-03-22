from django.contrib import admin

from .models import Object, Folder, File

admin.site.register(Object)
admin.site.register(Folder)
admin.site.register(File)