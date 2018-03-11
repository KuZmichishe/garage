# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import services
from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    devices = services.get_devices()
    dht22_sensors = services.get_sensors(2)

    return render(
        request,
        'hardware/index.html', {
            'devices': devices,
            'temperature': dht22_sensors,
        }
    )


def device_on(request, device_id):
    status = services.switch_device(int(device_id))
    if status:
        message = 'Turn off'
    else:
        message = 'Turn on'
    return JsonResponse({
        'success': status,
        'message': message
    })
