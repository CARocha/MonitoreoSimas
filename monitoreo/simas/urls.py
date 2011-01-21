import os
from django.conf.urls.defaults import *
from django.conf import settings
from models import Encuesta

urlpatterns = patterns('monitoreo.simas.views',
    (r'^index/$', 'inicio'),
    (r'^index/ajax/municipio/(?P<departamento>\d+)/$', 'get_municipios'),
    (r'^index/ajax/comunidad/(?P<municipio>\d+)/$', 'get_comunidad'),
    #graficas para los indicadores
    (r'^grafo/organizacion/(?P<tipo>\w+)/$', 'organizacion_grafos'),
    (r'^grafo/agua-disponibilidad/(?P<tipo>\d+)/$', 'agua_grafos_disponibilidad'),
    (r'^grafo/fincas/(?P<tipo>\w+)/$', 'fincas_grafos'),
    (r'^grafo/arboles/(?P<tipo>\w+)/$', 'arboles_grafos'),
    (r'^grafo/manejosuelo/(?P<tipo>\w+)/$', 'grafo_manejosuelo'),
    (r'^grafo/ingreso/(?P<tipo>\w+)/$', 'grafos_ingreso'),
    (r'^grafo/bienes/(?P<tipo>\w+)/$', 'grafos_bienes'),
    (r'^grafo/ahorro-credito/(?P<tipo>\w+)/$', 'ahorro_credito_grafos'),
    (r'^mapa/$', 'obtener_lista'),
    (r'^(?P<vista>\w+)/$', '_get_view'),
   
)
