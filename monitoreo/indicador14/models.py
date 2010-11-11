# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.simas.models import *

# Create your models here.

# Indicador 14 Otros ingresos.

class Fuentes(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Otros-Ingreso - Fuentes"
        #app_label = "Indicador 14 Otros Ingresos"
        #db_table = "simas_fuentes"

class TipoTrabajo(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Otro-Ingreso - TipoTrabajo"
        #app_label = "Indicador 14 Otros Ingresos"
        #db_table = "simas_tipotrabajo"

class OtrosIngresos(models.Model):
    '''Otros ingresos
    '''
    fuente = models.ForeignKey(Fuentes)
    tipo = models.ForeignKey(TipoTrabajo)
    meses = models.IntegerField('# Meses',null=True, blank=True)
    ingreso = models.IntegerField('Ingreso por mes',null=True, blank=True)
    tiene_ingreso = models.IntegerField(choices=CHOICE_MANEJA,null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.fuente.nombre
    
    class Meta:
        verbose_name_plural = "Otros Ingresos"
        #app_label = "Indicador 14 Otros Ingresos"
        #db_table = "simas_otrosingresos"

#-------------------------------------------------------------------------------
