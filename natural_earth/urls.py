
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^is_urban/$',  'natural_earth.views.is_urban', name='is_urban'),   
)

