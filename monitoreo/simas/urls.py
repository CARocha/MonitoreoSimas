import os
from django.conf.urls.defaults import *
from django.conf import settings
from models import Encuesta

urlpatterns = patterns('monitoreo.simas.views',
    (r'^index/$', 'inicio'),
    (r'^index/ajax/municipio/(?P<departamento>\d+)/$', 'get_municipios'),
    (r'^index/ajax/comunidad/(?P<municipio>\d+)/$', 'get_comunidad'),
    (r'^(?P<vista>\w+)/$', '_get_view'),
   
)
