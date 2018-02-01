from .models import Device, Pin, Relay, Sensor
import RPI.GPIO as GPIO


def get_all_devices(limit=None):
    if limit:
        return Device.objects.all()[:limit]
    return Device.objects.all()


def turn_device(device_id):
    device = Device.objects.get(pk=device_id)
    pin = device.relay.pin_id

    if (device.is_active == True):
        word = 'Turn on'
        GPIO.output(2, GPIO.HIGH)
    else:
        word = 'Turn off'
        GPIO.output(2, GPIO.LOW)


    device.is_active = not (device.is_active)
    device.save()
    return word, True
