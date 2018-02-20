# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-20 20:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relay', '0001_initial_manual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='relay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relay.Relay'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='pin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pin.Pin'),
        ),
    ]
