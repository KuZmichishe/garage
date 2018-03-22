CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_CONFIG = {
    'MOVEMENT_ACTIVE': (
        True,
        'This option allows you to activate automatic motion detection and devices control',
        bool
    ),
    'MOVEMENT_SENSOR_DELAY': (
        5,
        'Time in mins which device will be turned on until switched off',
        int
    ),
    'OUTSIDE_TEMPERATURE_SENSOR_ID': (
        1,
        'Id if sensor which is located outside, will be used in comparing',
        int
    ),
    'DIFFERENCE_IN_HUMIDITY': (
        1,
        'Difference (in %) between inside and outside sensor to activate device, related to inside sensor',
        int
    ),
    'MIN_TEMP_INSIDE': (
        3,
        'Minimum temperature which will trigger heater on',
        int
    ),
    'MAX_TEMP_INSIDE': (
        7,
        'Max temperature which will trigger heater off',
        int
    ),
    'AUTOMATIC_VENTILATE': (
        True,
        'Automatically switch coolers depend on humidity difference',
        bool
    ),
    'AUTOMATIC_HEAT': (
        True,
        'Automatically switch heater depend on min/max inside temperature',
        bool
    ),
}

CONSTANCE_CONFIG_FIELDSETS = {
    'Movement sensors': (
        'MOVEMENT_SENSOR_DELAY',
    ),
    'Climate sensors': (
        'OUTSIDE_TEMPERATURE_SENSOR_ID',
        'DIFFERENCE_IN_HUMIDITY',
        'MIN_TEMP_INSIDE',
        'MAX_TEMP_INSIDE',
    ),
    'Systems': (
        'MOVEMENT_ACTIVE',
        'AUTOMATIC_VENTILATE',
        'AUTOMATIC_HEAT',
    ),
}