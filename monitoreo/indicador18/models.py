# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.simas.models import *

# Create your models here.

# Indicador 18. Seguridad alimentaria
CHOICE_CATEGORIA = (
                        (1,'Carbohidrátos'),
                        (2,'Grasas'),
                        (3,'Minerales/Vitaminas'),
                        (4,'Proteinas')
                    )

class Alimentos(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.IntegerField(choices=CHOICE_CATEGORIA, null=True, blank=True)
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Seguridad-Alimento"

class Seguridad(models.Model):
    ''' Modelo Seguridad alimentaria
    '''
    alimento = models.ForeignKey(Alimentos)
    producen = models.IntegerField('Producen en la finca', choices=CHOICE_OPCION)
    compran = models.IntegerField('Compran para completar la necesidad', choices=CHOICE_OPCION)
    consumen = models.IntegerField('Consumen lo necesario en los meses de verano', choices=CHOICE_OPCION)
    consumen_invierno = models.IntegerField('Consumen lo necesario en los meses de invierno', choices=CHOICE_OPCION)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.alimento.nombre
    
    class Meta:
        verbose_name_plural = "Seguridad"
       
#-------------------------------------------------------------------------------
