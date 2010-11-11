# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.simas.models import *

# Create your models here.

# Indicador 7. Reforestación (periodo de referencia de mayo 2009 a abril 2010)

class Actividad(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Actividades de reforestacion"
        #app_label = "Indicador 07 Reforestacion"
        #db_table = "simas_actividad"

class Reforestacion(models.Model):
    ''' reforestacion
    '''
    reforestacion = models.ForeignKey(Actividad, verbose_name="Actividades de reforestación")
    cantidad = models.IntegerField('Cantidad de arboles sembrados')
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.reforestacion.nombre
    
    class Meta:
        verbose_name_plural = "Reforestacion"
        #app_label = "Indicador 07 Reforestacion"
        #db_table = "simas_reforestacion"

#-------------------------------------------------------------------------------
