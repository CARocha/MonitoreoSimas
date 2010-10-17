from models import *
from django.http import HttpResponse
from django.utils import simplejson

def get_municipios(request, departamento):
    municipios = Municipio.objects.filter(departamento = departamento)
    lista = [(municipio.id, municipio.nombre) for municipio in municipios]
    return HttpResponse(simplejson.dumps(lista), mimetype='application/javascript')

#def get_comunidad(request, municipio):
#    comunidades = Comunidad.objects.filter(municipio = municipio)
#    lista = [(comunidad.id, comunidad.nombre) for comunidad in comunidades]
#    return HttpResponse(simplejson.dumps(lista), mimetype='application/javascript')
