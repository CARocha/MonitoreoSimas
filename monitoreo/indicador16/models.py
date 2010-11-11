# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.simas.models import *

# Create your models here.

# Indicador 16. Ahorro

CHOICE_AHORRO = ((1,"Si"),(2,"No"),(3,"Menos de 5 años"),
                 (4,"Mas de 5 años"),(5,"Hombre"),(6,"Mujer"),
                 (7,"Ambos"))
class AhorroPregunta(models.Model):
    nombre = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = "Ahorro-Preguntas"   
    def __unicode__(self):
        return self.nombre
    
class Ahorro(models.Model):
    ''' modelos ahorro
    '''
    ahorro = models.ForeignKey(AhorroPregunta)
    respuesta = models.IntegerField(choices=CHOICE_AHORRO)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return self.ahorro.nombre
    
    class Meta:
        verbose_name_plural = "Ahorro"
        #app_label = "Indicador 16 Ahorro"
        #db_table = "simas_ahorro"

#-------------------------------------------------------------------------------
