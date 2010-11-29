# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from monitoreo.simas.models import *
from monitoreo.lugar.models import *

ANOS_CHOICES = ((2010,'2010'),(2011,'2011'),(2012,'2012'),(2013,'2013'),(2014,'2014'))
CHOICE_OPCION_F = (('','----'),(1,'Si'),(2,'No'))
CHOICE_DESDE_F = (('','----'),(1,"Menos de 5 año"),(2,"Mas de 5 años"))
CHOICE_DUENO_F = (('','----'),(1,"Hombre"),(2,"Mujer"),(3,"Mancomunado"),(4,"Parientes"),(5,"Colectivo"),(6,"No hay"))

class MonitoreoForm(forms.Form):
    fecha = forms.ChoiceField(choices=ANOS_CHOICES)
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(), 
            required=False, empty_label="Todos los Departamentos")
    municipio = forms.CharField(widget = forms.Select, required=False)
    comunidad = forms.CharField(widget = forms.Select, required=False)
    #organizacion = forms.ModelChoiceField(required = False, 
    #                                     queryset=Organizaciones.objects.all())
    socio = forms.ChoiceField(choices = CHOICE_OPCION_F , required=False)
    desde = forms.ChoiceField(choices = CHOICE_DESDE_F , required=False)
    dueno = forms.ChoiceField(label = 'Dueño', choices = CHOICE_DUENO_F , required=False)
