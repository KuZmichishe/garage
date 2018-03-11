# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Sensor, Sensor_Devices


class ChoiceInline(admin.StackedInline):
    model = Sensor_Devices
    extra = 1


class SensorAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_object', 'pin')
    fieldsets = [
        ('Main', {'fields': ['name', 'pin', 'type', 'code', 'result', 'fake']}),
        ('Media', {'fields': ['image', 'scheme_image']}),

    ]
    inlines = [ChoiceInline]


class Sensor_DevicesAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'device', 'type')

admin.site.register(Sensor, SensorAdmin)
admin.site.register(Sensor_Devices, Sensor_DevicesAdmin)
