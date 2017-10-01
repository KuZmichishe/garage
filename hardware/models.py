# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Pin(models.Model):
    number = models.IntegerField(null=False)
    name = models.CharField(null=False, max_length=100)
    is_in = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    position = models.IntegerField(null=False)


class Relay(models.Model):
    NUMBER_CHOICES = (
        ('1', 'First'),
        ('2', 'Second'),
        ('3', 'Third'),
        ('4', 'Forth'),
        ('5', 'Fifth'),
        ('6', 'Sixth'),
        ('7', 'Seventh'),
        ('8', 'Eughth'),
    )
    number = models.IntegerField(max_length=10, choices=NUMBER_CHOICES)
    pin = models.ForeignKey(Pin)


class Device(models.Model):
    name = models.CharField(null=False, max_length=100)
    pin = models.ForeignKey(Pin, through='Relay')
    realy = models.ForeignKey(Relay)


class Sensor(models.Model):
    name = models.CharField(null=False, max_length=100)
    pin = models.ForeignKey(Pin)
    realy = models.ForeignKey(Relay)
