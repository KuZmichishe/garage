#!/usr/bin/env python
import RPi.GPIO as GPIO
gpio_pin=27
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(gpio_pin, GPIO.OUT)
GPIO.output(gpio_pin, GPIO.HIGH)