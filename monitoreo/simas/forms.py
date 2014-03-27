# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from monitoreo.simas.models import *
from monitoreo.lugar.models import *

ANOS_CHOICES = ((2010,'2010'),(2011,'2011'),(2012,'2012'),(2013,'2013'),(2014,'2014'))
CHOICE_OPCION_F = (('','----'),(1,'Si'),(2,'No'))
CHOICE_DESDE_F = (('','----'),(1,"Menos de 5 año"),(2,"Mas de 5 años"))
CHOICE_DUENO_F = (('','----'),(1,"Hombre"),(2,"Mujer"),(3,"Mancomunado"),(4,"Parientes"),(5,"Colectivo"),(6,"No hay"))

def fecha_choice():
    years = []
    for en in Encuesta.objects.order_by('year').values_list('year', flat=True):
        years.append((en,en))
    return list(set(years))

def departamentos():   
    foo = Encuesta.objects.all().order_by('comunidad__municipio__departamento__nombre').distinct().values_list('comunidad__municipio__departamento__id', flat=True)
    return Departamento.objects.filter(id__in=foo)

class MonitoreoForm(forms.Form):
    fecha = forms.MultipleChoiceField(choices=fecha_choice())
    departamento = forms.ModelMultipleChoiceField(queryset=departamentos(), required=False, label=u'Departamentos')
    organizacion = forms.ModelMultipleChoiceField(queryset=Organizaciones.objects.all().order_by('nombre'), required=False, label=u'Organización')
    municipio = forms.ModelMultipleChoiceField(queryset=Municipio.objects.all().order_by('nombre'), required=False)
    comunidad = forms.ModelMultipleChoiceField(queryset=Comunidad.objects.all(), required=False)
    socio = forms.ChoiceField(choices = CHOICE_OPCION_F , required=False, label="Socio Gremial")
    desde = forms.ChoiceField(choices = CHOICE_DESDE_F , required=False)
    dueno = forms.ChoiceField(label = 'Dueño', choices = CHOICE_DUENO_F , required=False)

#modelos = [Educacion,Salud,Energia,Cocina,Agua,OrganizacionGremial,OrganizacionComunitaria,
#           UsoTierra,ExistenciaArboles,Reforestacion,AnimalesFinca,CultivosFinca,OpcionesManejo,
#           Semilla,Suelo,ManejoSuelo,IngresoFamiliar,OtrosIngresos,TipoCasa,DetalleCasa,
#           Propiedades,Herramientas,Transporte,Ahorro,Credito,Seguridad,Vulnerable,Riesgos,
#           Tenencia]
modelos = (
        ('1', 'Educacion'),('2', 'Salud'),('3', 'Energia'),
        ('4', 'Cocina'),('5', 'Agua'),('6', 'OrganizacionGremial'),
        ('7', 'OrganizacionComunitaria'),('8', 'UsoTierra'),
        ('9', 'ExistenciaArboles'),('10', 'Reforestacion'),
        ('11', 'AnimalesFinca'),('12', 'CultivosFinca'),
        ('13', 'OpcionesManejo'),('14', 'Semilla'),('15', 'Suelo'),
        ('16', 'ManejoSuelo'),('17', 'IngresoFamiliar'),
        ('18', 'OtrosIngresos'),('19', 'TipoCasa'),('20', 'DetalleCasa'),
        ('21', 'Propiedades'),('22', 'Herramientas'),('23', 'Transporte'),
        ('24', 'Ahorro'),('25', 'Credito'),('26', 'Seguridad'),('27', 'Vulnerable'),
        ('28', 'Riesgos'),('29', 'Tenencia'),
    )

class ExportarMonitoreoForm(forms.Form):
    fecha2 = forms.MultipleChoiceField(choices=ANOS_CHOICES, label=u'Fecha')
    departamento2 = forms.ModelMultipleChoiceField(queryset=departamentos(), required=False, 
                                                label=u'Departamentos')
    organizacion2 = forms.ModelMultipleChoiceField(queryset=Organizaciones.objects.all().order_by('nombre'), 
                                                required=False, label=u'Organización')
    municipio2 = forms.ModelMultipleChoiceField(queryset=Municipio.objects.all().order_by('nombre'), 
                                                required=False, label=u'Municipio')
    comunidad2 = forms.ModelMultipleChoiceField(queryset=Comunidad.objects.all(), 
                                                required=False, label=u'Comunidad')
    dueno2 = forms.ChoiceField(label = u'Dueño', choices = CHOICE_DUENO_F , 
                                                required=False)
    modelo = forms.MultipleChoiceField(choices=modelos, label=u'Modelos')
