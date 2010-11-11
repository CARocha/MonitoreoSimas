# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.simas.models import *

# Create your models here.

# Indicador 19. cuales son los riesgos que hace la finca vulnerable

class Causa(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Vulnerable - causa"
        #app_label = "Indicador 19 Riesgo Finca vulnerable"
        #db_table = "simas_causa"
        
class Fenomeno(models.Model):
    causa = models.ForeignKey(Causa)
    nombre = models.CharField(max_length=100)
    
    def __unicode__(self):
        return '%s - %s' % (self.causa.nombre, self.nombre)
        
    class Meta:
        verbose_name_plural = "Vulnerable - causa + fenomeno"
        #app_label = "Indicador 19 Riesgo Finca vulnerable"
        #db_table = "simas_fenomeno"
        
class Graves(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Vulnerable - daños graves"
        #app_label = "Indicador 19 Riesgo Finca vulnerable"
        #db_table = "simas_graves"
        
class Vulnerable(models.Model):
    ''' 20 modelo vulnerable
    '''
    motivo = models.ForeignKey(Fenomeno)
    respuesta = models.ManyToManyField(Graves, verbose_name="¿Casa cuanto hay daños graves en la finca?")
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Vulnerable"
        #app_label = "Indicador 19 Riesgo Finca vulnerable"
        #db_table = "simas_vulnerable"

#-------------------------------------------------------------------------------
