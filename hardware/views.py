# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import services
from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    devices = services.get_devices()
    temperature = services.get_sensors(2)

    return render(
        request,
        'hardware/index.html', {
            'devices': devices,
            'temperature': temperature,
        }
    )


def device_on(request, device_id):
    word, status = services.turn_device(device_id)
    return JsonResponse({
        'success': status,
        'message': word
    })


def update_temperature(request):
    temperature = services.get_sensors(2)
    for t in temperature:
        temp, hum = services.get_temp_hum(t.pin_id)
        t.result = 'Temp = {0:0.1f} °C,  Humidity = {1:0.1f} %'.format(temp, hum)
        t.save()
    return JsonResponse({
        'success': True,
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