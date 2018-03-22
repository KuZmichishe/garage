# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Device, Group
from image_cropping import ImageCroppingMixin


class DeviceAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('name', 'image_object', 'scheme_image_object')


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Device, DeviceAdmin)
admin.site.register(Group, GroupAdmin)
