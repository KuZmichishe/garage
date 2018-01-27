# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Pin, Relay, Device, Sensor, PinAdmin, DeviceAdmin


admin.site.register(Pin, PinAdmin)
admin.site.register(Relay)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Sensor)

