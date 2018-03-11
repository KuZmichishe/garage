# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from pin.models import Pin
from django.conf import settings


class Relay(models.Model):
    number = models.IntegerField(unique=True, choices=settings.RELAY_CHOICES)
    pin = models.ForeignKey(Pin)

    def __str__(self):
        return 'Relay ' + str(self.number)
