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


def do_climate_actions():
    out_sensor_data = get_temperature_humidity(config.OUTSIDE_TEMPERATURE_SENSOR_ID)
    results = {}
    for in_sensor in get_sensors(2).exclude(id=config.OUTSIDE_TEMPERATURE_SENSOR_ID):
        in_sensor_data = get_temperature_humidity(in_sensor.id)
        if config.AUTOMATIC_VENTILATE:
            results['humidity'] = check_humidity_difference(out_sensor_data[1], in_sensor_data[1], in_sensor)
        if config.AUTOMATIC_HEAT:
            results['temperature'] = check_inside_temperature(out_sensor_data[0], in_sensor_data[0], in_sensor)
    return results


def check_humidity_difference(out_sensor_hum, in_sensor_hum, in_sensor):
    results = {}
    if in_sensor_hum - out_sensor_hum > config.DIFFERENCE_IN_HUMIDITY:
        action = True
    elif in_sensor_hum - out_sensor_hum <= config.DIFFERENCE_IN_HUMIDITY:
        action = False
    for device in in_sensor.devices.all().filter(sensor_devices__type=2):
        switch_device(device.id, action)
        results[str(device.name)] = {
            'device_name': device.name,
            'action': action,
            'out_sensor_hum': out_sensor_hum,
            'in_sensor_hum': in_sensor_hum,
            'difference': in_sensor_hum - out_sensor_hum
        }
    return results


def check_inside_temperature(out_sensor_temp, in_sensor_temp, in_sensor):
    results = {}
    if in_sensor_temp <= config.MIN_TEMP_INSIDE:
        action = True
    elif (in_sensor >= config.MAX_TEMP_INSIDE) or (out_sensor_temp >= config.MIN_TEMP_INSIDE):
        action = False
    for device in in_sensor.devices.all().filter(sensor_devices__type=1):
        switch_device(device.id, action)
        results[str(device.name)] = {
            'device_name': device.name,
            'action': action,
            'out_sensor_temp': out_sensor_temp,
            'in_sensor_temp': in_sensor_temp,
        }
    return results


def get_temperature_humidity(sensor_id):
    sensor = Sensor.objects.get(pk=sensor_id)
    if sensor.fake:
        data = get_dht22_data_fake()
    else:
        data = get_dht22_data(int(sensor.pin.number))
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
