# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-11 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pin', '0002_auto_20180220_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='pin',
            name='position',
            field=models.IntegerField(unique=True),
        ),
    ]
