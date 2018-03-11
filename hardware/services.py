from .models import Device
from sensor.models import Sensor, TemperatureHistory
import RPi.GPIO as GPIO
import Adafruit_DHT
from datetime import datetime
from constance import config


def get_devices(limit=None):
    if limit:
        return Device.objects.all()[:limit]
    return Device.objects.all()


def get_sensors(type=1, limit=None):
    if limit:
        return Sensor.objects.filter(type=type)[:limit]
    return Sensor.objects.filter(type=type)


def check_humidity_difference():
    out_sensor_data = get_temperature_humidity(config.OUTSIDE_TEMPERATURE_SENSOR_ID)
    for in_sensor in get_sensors(2).exclude(id=config.OUTSIDE_TEMPERATURE_SENSOR_ID):
        in_sensor_data = get_temperature_humidity(in_sensor.id)
        if out_sensor_data[1] - in_sensor_data[1] >= config.DIFFERENCE_IN_HUMIDITY:
            for device in in_sensor.devices.all():
                switch_device(device.id, True)
        else:
            if out_sensor_data[1] - in_sensor_data[1] <= 0:
                for device in in_sensor.devices.all():
                    switch_device(device.id, False)
    return True


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


def get_temperature_humidity(sensor_id):
    sensor = Sensor.objects.get(pk=sensor_id)
    data = get_dht22_data(sensor.pin.id)
    return data


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
