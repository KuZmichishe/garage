# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-20 21:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relay', '0002_auto_20180220_2024'),
    ]

    stateOperations = [
        migrations.RemoveField(
            model_name='relay',
            name='device',
        ),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(None, state_operations=stateOperations)
    ]
