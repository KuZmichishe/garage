import random


def DHT22():
    return 2


def read_retry(sensor, pin):
    return random.randint(1, 50), random.randint(20, 100)
