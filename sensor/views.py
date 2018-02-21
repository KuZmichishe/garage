# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from .models import Sensor
from django.core.serializers import serialize


def index(request):
    sensors = Sensor.objects.filter(type=2)
    # .filter(temperaturehistory__requested_date__minute=10)
    return render(
        request,
        'sensor/index.html', {
            'sensors': sensors,
        }
    )
