# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.conf import settings
from django.utils.html import format_html
from django.conf.urls.static import static


class Pin(models.Model):
    number = models.IntegerField(null=False)
    name = models.CharField(null=False, max_length=100)
    is_in = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    position = models.IntegerField(null=False)

    def __str__(self):
        return self.name + '-' + str(self.position)


class PinAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_in', 'is_active', 'position')


class Device(models.Model):
    name = models.CharField(null=False, max_length=100)
    pin = models.ManyToManyField(Pin, through='Relay')
    image = models.FileField(default='')
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


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_object', 'scheme_image_object')


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
    device = models.ForeignKey(Device)

    def __str__(self):
        return 'Relay ' + self.number


class Sensor(models.Model):
    name = models.CharField(null=False, max_length=100)
    pin = models.ForeignKey(Pin)
    image = models.FileField(default='')
    scheme_image = models.FileField(default='')

    def __str__(self):
        return self.name
