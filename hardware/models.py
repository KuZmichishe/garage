# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from image_cropping import ImageRatioField, ImageCroppingMixin
from pin.models import Pin
from relay.models import Relay


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


class DeviceAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('name', 'image_object', 'scheme_image_object')
