# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-22 21:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('object', '0003_auto_20160322_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='subfolder',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='object.Folder'),
        ),
    ]