# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.apps import AppConfig
import subprocess


class HardwareConfig(AppConfig):
    name = 'hardware'

    def ready(self):
        subprocess.Popen(['python', '/home/pi/projects/garage/hardware/test.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
