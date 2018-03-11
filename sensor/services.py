from hardware.services import switch_device
from constance import config
import Adafruit_DHT
from datetime import datetime
import random
from models import Sensor, TemperatureHistory


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
    return out_sensor_data[1] - in_sensor_data[1]


def get_temperature_humidity(sensor_id):
    sensor = Sensor.objects.get(pk=sensor_id)
    if sensor.fake:
        data = get_dht22_data_fake()
    else:
        data = get_dht22_data(sensor.pin.id)
    return data


def get_dht22_data(pin):
    sensor = Adafruit_DHT.DHT22
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        return temperature, humidity
    else:
        return


def get_dht22_data_fake():
    return random.randint(1, 10), random.randint(1, 10)


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
