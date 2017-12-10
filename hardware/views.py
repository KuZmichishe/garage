# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Device, Pin, Relay, Sensor
from django.http import JsonResponse
from django.core.serializers import serialize


def index(request):
    devices = Device.objects.all()
    return render(
        request,
        'hardware/index.html',
        {
            'devices': devices,
        }
    )


def device_on(request, device_id):
    device = Device.objects.get(pk=device_id)
    return render(request, 'hardware/device_on.html', {'device': device})
    #JsonResponse({'sucess': device})
