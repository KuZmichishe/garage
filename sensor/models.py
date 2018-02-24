# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.conf import settings
from pin.models import Pin
from hardware.models import Device


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

    def history_hourly(self):
        return TemperatureHistory.objects.filter(
            sensor__exact=self.id,
            requested_date__minute=10,
        )

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
    temperature = models.DecimalField(null=True, max_digits=3, decimal_places=1)
    humidity = models.DecimalField(null=True, max_digits=3, decimal_places=1)

