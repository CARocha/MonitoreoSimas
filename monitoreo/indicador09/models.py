# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.simas.models import *

# Create your models here.

# Indicador 9. Cultivos en la finca (periodo de referencia de mayo 2009 a abril 2010)

class Cultivos(models.Model):
    nombre = models.CharField(max_length=50)
    unidad = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "CultivosFinca-Cultivos"
        #app_label = "Indicador 09 cultivos en la finca"
        #db_table = "simas_cultivos"


class CultivosFinca(models.Model):
    ''' indicador cultivos en la finca
    '''
    cultivos = models.ForeignKey(Cultivos)
    area =  models.FloatField('Área/Mz')
    total = models.FloatField('Total producción por año')
    consumo = models.FloatField('Consumo por año')
    venta_libre = models.FloatField('Venta libre por año')
    venta_organizada = models.FloatField('Venta organizada por año')
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.cultivos.nombre
    
    class Meta:
        verbose_name_plural = "Cultivos en la finca"
        #app_label = "Indicador 09 cultivos en la finca"
        #db_table = "simas_cultivosfinca"

#-------------------------------------------------------------------------------
