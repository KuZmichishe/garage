from django.conf.urls import url
from . import views


app_name = 'hardware'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^device_on/(?P<device_id>[0-9]+)/$', views.device_on, name='device_on'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
]
