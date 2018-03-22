# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import services
import sensor.services
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import UserForm


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'hardware/login.html')
    else:
        devices = services.get_devices()
        dht22_sensors = sensor.services.get_sensors(2)

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


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'hardware/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                devices = services.get_devices()
                return render(request, 'hardware/index.html', {'devices': devices})
            else:
                return render(request, 'hardware/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'hardware/login.html', {'error_message': 'Invalid login'})
    return render(request, 'hardware/login.html')
