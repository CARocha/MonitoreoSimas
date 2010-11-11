# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.simas.models import *

# Create your models here.

# Indicador 5 Uso de Tierrra

class Uso(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Uso de tierra"
        #app_label = "Indicador 05 Uso de Tierra"
        #db_table = "simas_uso"

class UsoTierra(models.Model):
    ''' Uso de tierra
    '''
    tierra = models.ForeignKey(Uso, verbose_name="Uso de Tierra")
    area = models.FloatField('Área en Mz')
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.tierra.nombre

#-------------------------------------------------------------------------------
