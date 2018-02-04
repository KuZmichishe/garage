# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from image_cropping import ImageRatioField, ImageCroppingMixin
from django.conf import settings


class Pin(models.Model):
    number = models.IntegerField(null=False)
    name = models.CharField(null=False, max_length=100)
    is_in = models.BooleanField(default=True)
    position = models.IntegerField(null=False)

    def __str__(self):
        return self.name + '-' + str(self.position)


class PinAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_in', 'position')


class Relay(models.Model):
    NUMBER_CHOICES = (
        (1, 'First'),
        (2, 'Second'),
        (3, 'Third'),
        (4, 'Forth'),
        (5, 'Fifth'),
        (6, 'Sixth'),
        (7, 'Seventh'),
        (8, 'Eighth'),
    )
    number = models.IntegerField(choices=NUMBER_CHOICES)
    pin = models.ForeignKey(Pin)

    def __str__(self):
        return 'Relay ' + str(self.number)


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


class Sensor(models.Model):
    name = models.CharField(null=False, max_length=100)
    pin = models.ForeignKey(Pin)
    devices = models.ManyToManyField(Device, blank=True)
    type = models.IntegerField(choices=settings.SENSOR_TYPE, default=3)
    image = models.FileField(default='')
    scheme_image = models.FileField(default='')
    code = models.CharField(null=False, max_length=100, default='')
    last_request_time = models.DateTimeField(blank=True, auto_now=True)
    result = models.CharField(blank=True, max_length=200)

    @property
    def history_items(self):
        return TemperatureHistory.objects.filter(sensor__exact=self.id)

    def __str__(self):
        return self.name

    def image_object(self):
        return format_html(
            '<img width=30 height=30 src="{}" />',
            self.image.url,
        )


class SensorAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_object', 'pin')


class TemperatureHistory(models.Model):
    requested_date = models.DateTimeField()
    sensor = models.ForeignKey(Sensor, null=True)
    temperature = models.IntegerField(null=True)
    humidity = models.IntegerField(null=True)
