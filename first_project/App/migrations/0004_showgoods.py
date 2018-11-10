# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-09 02:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20181101_0710'),
    ]

    operations = [
        migrations.CreateModel(
            name='Showgoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goodsid', models.CharField(max_length=50)),
                ('img', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=50)),
                ('span1', models.CharField(max_length=50)),
                ('span2', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'app_showgoods',
            },
        ),
    ]