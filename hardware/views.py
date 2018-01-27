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
        'hardware/index.html', {
            'devices': devices,
        }
    )


def device_on(request, device_id):
    device = Device.objects.get(pk=device_id)
    pin = device.relay.pin_id

    if(device.is_active == True):
        word = 'Turn on'
    else:
        word = 'Turn off'

    device.is_active = not(device.is_active)
    device.save()
    return JsonResponse({
        'success': True,
        'message': word
    })


'''
def hcsr501(request):
    import RPi.GPIO as GPIO
    import time
    GPIO.setmode(GPIO.BCM)
    pir = 5
    GPIO.setup(pir, GPIO.IN)

    print ("Waiting for sensor to settle")
    time.sleep(2)
    print ("Detecting motion")
    while True:
        if GPIO.input(pir):
            print ("Motion Detected!")
            time.sleep(2)
        time.sleep(0.1)


def dht22(request):
    import Adafruit_DHT
    sensor = Adafruit_DHT.DHT22
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')
    return
'''