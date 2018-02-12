#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/projects/garage/
sudo python manage.py runserver 0.0.0.0:80
cd hardware/
sudo python test.py
cd /