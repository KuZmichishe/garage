# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from .models import Sensor, TemperatureHistory
from django.core.serializers import serialize


def index(request):
    sensors = Sensor.objects.filter(type=2).select_related()
    for i, sensor in enumerate(sensors):
        sensors[i].temp = TemperatureHistory.objects.filter(
            requested_date__minute=00,
            sensor_id=sensor.id,
        )
    return render(
        request,
        'sensor/index.html', {
            'sensors': sensors,
        }
    )
