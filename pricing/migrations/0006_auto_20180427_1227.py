# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-27 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0005_auto_20180425_1437'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='update_time',
            new_name='time',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='publish_time',
        ),
        migrations.AddField(
            model_name='listing',
            name='new',
            field=models.BooleanField(default=True),
        ),
    ]