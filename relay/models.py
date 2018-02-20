# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from pin.models import Pin


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
