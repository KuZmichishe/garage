# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-20 21:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0015_merge_20180220_2049'),
    ]

    database_operations = [
        migrations.AlterModelTable('Sensor', 'sensor_sensor'),
        migrations.AlterModelTable('TemperatureHistory', 'sensor_temperaturehistory'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=database_operations,
        )
    ]
