# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.html import format_html
from image_cropping import ImageRatioField
from pin.models import Pin
from relay.models import Relay
from django.conf import settings


class Device(models.Model):
    name = models.CharField(null=False, max_length=100)
    relay = models.ForeignKey(Relay)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(blank=True, upload_to='uploaded_images')
    cropped_image = ImageRatioField('image', '422x422')
    scheme_image = models.FileField(default='')

    def image_object(self):
        return format_html(
            '<img width=30 height=30 src="{}" />',
            self.image.url,
        )

    def scheme_image_object(self):
        return format_html(
            '<img width=30 height=30 src="{}" />',
            self.scheme_image.url,
        )

    image_object.admin_order_field = 'image'
    scheme_image_object.admin_order_field = 'scheme_image'

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(null=False, max_length=100)
    device = models.ManyToManyField(Device)


class Schedule(models.Model):
    device = models.ForeignKey(Device)
    start_time = models.DateTimeField(auto_now=True)
    type = models.IntegerField(choices=settings.SCHEDULE_TYPE)
