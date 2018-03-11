# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import services, pin.services, hardware.services

from django.shortcuts import render
from .models import Sensor, TemperatureHistory
from .forms import FiltersForm
from django.db.models import Q
from django.db.models.functions import TruncDay
from django.http import JsonResponse
from constance import config
from django.utils import timezone, dateparse


def index(request):
    if request.method == 'POST':
        form = FiltersForm(request.POST)
        if form.is_valid():
            filter = Q(requested_date__gt=form.cleaned_data['date_from']) & Q(requested_date__lt=form.cleaned_data['date_to'])
    else:
        form = FiltersForm()
        # now = timezone.now()
    sensors = Sensor.objects.filter(type=2)
    for i, sensor in enumerate(sensors):
        sensors[i].temp = TemperatureHistory.objects.filter(
            sensor_id=sensor.id,
        ).annotate(
            date=TruncDay('requested_date'),
        )
        if request.method == 'POST':
            sensors[i].temp = sensors[i].temp.filter(filter)
    return render(
        request,
        'sensor/index.html', {
            'sensors': sensors,
            'form': form
        }
    )


def update_temperature(request):
    dht22_sensors = services.get_sensors(2)
    for dht22_sensor in dht22_sensors:
        temp, hum = services.get_dht22_data(int(dht22_sensor.pin.number))
        dht22_sensor.result = 'Temp = {0:0.1f} °C,  Humidity = {1:0.1f} %'.format(temp, hum)
        dht22_sensor.save()
        services.register_temperature(temp, hum, dht22_sensor)
    return JsonResponse({
        'success': True,
    })


def check_motion(request):
    state = False
    if config.MOVEMENT_ACTIVE:
        hcsr501_sensors = list(services.get_sensors(3))
        duration = dateparse.parse_duration('0:' + str(config.MOVEMENT_SENSOR_DELAY) + ':0')
        for hcsr501_sensor in hcsr501_sensors:
            devices = hcsr501_sensor.devices.all()
            if pin.services.detect_movement(int(hcsr501_sensor.pin.number)):
                hcsr501_sensor.last_request_time = timezone.now()
                hcsr501_sensor.save()
                state = True
                for device in devices:
                    if not device.is_active:
                        hardware.services.switch_device(int(device.id), state)
                        print(1)
            else:
                if timezone.now() - hcsr501_sensor.last_request_time > duration:
                    for device in devices:
                        if device.is_active:
                            hardware.services.switch_device(int(device.id), state)
                            print(2)
    return JsonResponse({'Status': state})


def check_humidity(request):
    difference = services.check_humidity_difference()
    return JsonResponse({
        'success': difference,
    })
