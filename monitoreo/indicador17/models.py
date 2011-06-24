# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.simas.models import *

# Create your models here.

# Indicador 17. Crédito en efectivo o materiales

class DaCredito(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Credito-Dacredito"


class OcupaCredito(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Credito-Ocupa"


CHOICE_SATISFACCION = ((1,"Menos de 25 % de las necesidades"),
                       (2,"Entre 25 y 50 % de las necesidades"),
                       (3,"Entre 50 y 100 % de las necesidades"),
                       (4,"No aplica"))

class Credito(models.Model):
    ''' Modelo de credito
    '''
    recibe = models.IntegerField('Recibe Crédito', choices= CHOICE_OPCION,
                                 null=True, blank=True)
    desde = models.IntegerField('Desde cuando', choices= CHOICE_DESDE,
                                 null=True, blank=True)
    quien_credito = models.ManyToManyField(DaCredito, verbose_name="De quien recibe credito",
                                           null=True, blank=True)
    ocupa_credito = models.ManyToManyField(OcupaCredito, verbose_name="Para que ocupa el credito",
                                           null=True, blank=True)
    satisfaccion = models.IntegerField('Satisfacción de la demanda de crédito',
                                       choices= CHOICE_SATISFACCION, blank=True, null=True)
    dia = models.IntegerField('Esta al dia con su Crédito', choices=CHOICE_OPCION,
                              null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.get_recibe_display()
    
    class Meta:
        verbose_name_plural = "Credito"
        #app_label = "Indicador 17 Credito"
        #db_table = "simas_credito"

#-------------------------------------------------------------------------------
