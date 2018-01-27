# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-27 20:46
from __future__ import unicode_literals

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0004_auto_20180125_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='cropped_image',
            field=image_cropping.fields.ImageRatioField('image', '430x360', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropped image'),
        ),
        migrations.AlterField(
            model_name='device',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploaded_images'),
        ),
    ]