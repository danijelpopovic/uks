# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='isPrivate',
            field=models.BooleanField(default=True),
        ),
    ]
