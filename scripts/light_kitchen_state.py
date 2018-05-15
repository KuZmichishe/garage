#!/usr/bin/env python
# -*- coding utf-8 -*-
import subprocess
from subprocess import Popen, PIPE

gpio_pin=17
proc = Popen(
        "echo %s > /sys/class/gpio/export" % gpio_pin,
        shell=True,
        stdout=PIPE, stderr=PIPE
)

proc.wait()
proc = Popen(
        "cat /sys/class/gpio/gpio%s/value" % gpio_pin,
        shell=True,
        stdout=PIPE, stderr=PIPE
)

proc.wait()
res = proc.communicate()
count = res[0].replace("\n", "")
count = int(count)

if count == 0:
        print('1').replace("\n","")
else:
        id=0