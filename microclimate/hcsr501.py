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
