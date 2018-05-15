from django.conf.urls import url
from . import views


app_name = 'sensor'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^update/temperature/$', views.update_temperature, name='update_temperature'),
    url(r'^check/motion/$', views.check_motion, name='check_motion'),
    url(r'^check/climate/$', views.check_climate, name='check_climate'),
    url(r'^temperature/json$', views.get_temp_inside_json, name='get_temp_inside_json'),
]
