# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-03 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0006_auto_20180131_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='last_request_time',
            field=models.DateTimeField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensor',
            name='result',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
