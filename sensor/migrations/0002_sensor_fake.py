# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-11 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='fake',
            field=models.BooleanField(default=False),
        ),
    ]
