# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-11 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0004_auto_20180311_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor_devices',
            name='type',
            field=models.IntegerField(choices=[(1, b'Other'), (2, b'Temperature'), (3, b'Movement')], default=1),
        ),
    ]
