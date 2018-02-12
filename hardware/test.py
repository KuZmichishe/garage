import urllib2
import time


time.sleep(5)
while True:
    response = urllib2.urlopen('http://garage.kuzmich.xyz:8000/check/motion/')
    html = response.read()
    print(html)
    time.sleep(2)
