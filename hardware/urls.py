from django.conf.urls import url
from . import views


app_name = 'hardware'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^device_on/(?P<device_id>[0-9]+)/$', views.device_on, name='device_on'),
    url(r'^update_temperature/$', views.update_temperature, name='update_temperature'),
    url(r'^check_motion/$', views.check_motion, name='check_motion'),
]
