# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-03 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0008_auto_20180203_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='result',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
