# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin


class Pin(models.Model):
    number = models.IntegerField(null=False)
    name = models.CharField(null=False, max_length=100)
    is_in = models.BooleanField(default=True)
    position = models.IntegerField(null=False)

    def __str__(self):
        return self.name + '-' + str(self.position)


class PinAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_in', 'position')
