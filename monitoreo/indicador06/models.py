# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.simas.models import *

class Maderable(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Arboles maderables"
        #app_label = "Indicador 06 existencia de arboles"
        #db_table = "simas_maderable"

class Forrajero(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Arboles forrageros"
        #app_label = "Indicador 06 existencia de arboles"
        #db_table = "simas_forrajero"

class Energetico(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Arboles energeticos"
        #app_label = "Indicador 06 existencia de arboles"
        #db_table = "simas_energetico"

class Frutal(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Arboles frutal"
        #app_label = "Indicador 06 existencia de arboles"
        #db_table = "simas_frutal"

class ExistenciaArboles(models.Model):
    ''' Existencia de arboles en la finca
        por tipo de uso
    '''
    maderable = models.ManyToManyField(Maderable, verbose_name="Maderable")
    cantidad_maderable = models.IntegerField()
    forrajero = models.ManyToManyField(Forrajero, verbose_name="Forrajero")
    cantidad_forrajero = models.IntegerField()
    energetico = models.ManyToManyField(Energetico, verbose_name="Energetico")
    cantidad_energetico = models.IntegerField()
    frutal = models.ManyToManyField(Frutal, verbose_name="Frutal")
    cantidad_frutal = models.IntegerField()
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = " Existencia de Arboles"
        #app_label = "Indicador 06 existencia de arboles"
        #db_table = "simas_existenciaarboles"

#-------------------------------------------------------------------------------
