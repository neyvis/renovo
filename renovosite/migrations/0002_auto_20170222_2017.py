# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 20:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('renovosite', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Services',
            new_name='Service',
        ),
    ]
