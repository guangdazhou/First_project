# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-01 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_wheel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='tel',
        ),
        migrations.AddField(
            model_name='user',
            name='RPwd',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]
