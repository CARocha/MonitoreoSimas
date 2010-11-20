# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.simas.models import *

# Create your models here.

# Indicador 20. Mitigación de riesgos

class PreguntaRiesgo(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Riesgo - pregunta"
        #app_label = "Indicador 20 Mitigacion de riesgos"
        #db_table = "simas_preguntariesgo"

class Riesgos(models.Model):
    ''' 20 mitigacion de los riesgos
    '''
    pregunta = models.ForeignKey(PreguntaRiesgo)
    respuesta = models.IntegerField('Respuesta', choices=CHOICE_OPCION)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Riesgos"
        #app_label = "Indicador 15 Propiedades y Bienes"
        #db_table = "simas_riesgos"

#-------------------------------------------------------------------------------
