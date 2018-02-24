# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-20 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relay', '0001_initial_manual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relay',
            name='number',
            field=models.IntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Forth'), (5, 'Fifth'), (6, 'Sixth'), (7, 'Seventh'), (8, 'Eighth')]),
        ),
        migrations.AlterModelTable(
            name='relay',
            table=None,
        ),
    ]