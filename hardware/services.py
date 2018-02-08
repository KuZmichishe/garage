from .models import Device, Pin, Relay, Sensor, TemperatureHistory
import RPi.GPIO as GPIO
import Adafruit_DHT
from datetime import datetime
import time


def get_devices(limit=None):
    if limit:
        return Device.objects.all()[:limit]
    return Device.objects.all()


def get_sensors(type=1, limit=None):
    if limit:
        return Sensor.objects.filter(type=type)[:limit]
    return Sensor.objects.filter(type=type)


def switch_device(device_id, state=None):
    device = Device.objects.get(pk=device_id)
    pin = device.relay.pin.number
    if state is None:
        state = not device.is_active
    switch_pin(int(pin), not state)
    device.is_active = state
    device.save()
    return state


def switch_pin(pin, output=GPIO.HIGH, pin_mode=GPIO.OUT, mode=GPIO.BCM):
    GPIO.setmode(mode)
    GPIO.setup(pin, pin_mode)
    GPIO.output(pin, output)
    return True


def get_dht22_data(pin):
    sensor = Adafruit_DHT.DHT22
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        return temperature, humidity
    else:
        return


def register_temperature(temp, hum, sensor_id):
    history = TemperatureHistory(
        requested_date=datetime.now(),
        sensor=sensor_id,
        temperature=temp,
        humidity=hum
    )
    try:
        history.save()
    except Exception as inst:
        print(inst.args)
        print(inst.message)
    return


def detect_movement(pin, pin_mode=GPIO.IN, mode=GPIO.BCM):
    GPIO.setmode(GPIO.BCM)
    GPIO.setmode(mode)
    GPIO.setup(pin, pin_mode)

    if GPIO.input(pin):
        return True
    return False
