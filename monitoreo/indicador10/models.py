# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.simas.models import *

# Create your models here.

# Indicador 10. Opciones de manejo agroecologico

class ManejoAgro(models.Model):
    nombre = models.CharField(max_length=50)
    unidad = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Uso opciones de manejo agroecologico"

CHOICE_NIVEL_CONOCIMIENTO = ((1,'Nada'),
                             (2,'Poco'),
                             (3,'Algo'),
                             (4,'Bastante'))

class OpcionesManejo(models.Model):
    ''' opciones de manejo agroecologico
    '''
    uso = models.ForeignKey(ManejoAgro, verbose_name="Uso de opciones de manejo agroecologico")
    nivel = models.IntegerField('Nivel de conocimiento', choices=CHOICE_NIVEL_CONOCIMIENTO)
    menor_escala = models.IntegerField('Han experimentado en pequeña escala', choices=CHOICE_OPCION)
    mayor_escala = models.IntegerField('Han experimentado en mayor escala', choices=CHOICE_OPCION)
    volumen = models.FloatField('¿Qué área, número o volumen')
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.uso.nombre
    
    class Meta:
        verbose_name_plural = "Opciones de manejo"

#-------------------------------------------------------------------------------
