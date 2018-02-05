import urllib2
import time

while True:
    response = urllib2.urlopen('http://garage.kuzmich.xyz:8000/check_motion/')
    html = response.read()
    print(html)
    time.sleep(2)
