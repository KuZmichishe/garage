#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd "$(dirname "$0")"
sudo python manage.py runserver 0.0.0.0:80
cd /