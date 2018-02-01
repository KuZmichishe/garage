from .models import Device, Pin, Relay, Sensor
import RPi.GPIO as GPIO


def get_all_devices(limit=None):
    if limit:
        return Device.objects.all()[:limit]
    return Device.objects.all()


def turn_device(device_id):
    device = Device.objects.get(pk=device_id)
    pin = device.relay.pin.number

    if device.is_active:
        word = 'Turn on'
        turn_pin_on_off(int(pin))
    else:
        word = 'Turn off'
        turn_pin_on_off(int(pin), GPIO.LOW)

    device.is_active = not device.is_active
    device.save()
    return word, True


def turn_pin_on_off(pin, output=GPIO.HIGH, pin_mode=GPIO.OUT, mode=GPIO.BCM):
    GPIO.setmode(mode)
    GPIO.setup(pin, pin_mode)
    GPIO.output(pin, output)
    return True
