import RPi.GPIO as GPIO


def switch_pin(pin, output=GPIO.HIGH, pin_mode=GPIO.OUT, mode=GPIO.BCM):
    GPIO.setmode(mode)
    GPIO.setup(pin, pin_mode)
    GPIO.output(pin, output)
    return True


def detect_movement(pin, pin_mode=GPIO.IN, mode=GPIO.BCM):
    GPIO.setmode(GPIO.BCM)
    GPIO.setmode(mode)
    GPIO.setup(pin, pin_mode)

    if GPIO.input(pin):
        return True
    return False
