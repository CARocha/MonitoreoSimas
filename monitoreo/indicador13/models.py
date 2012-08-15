# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.simas.models import *

# Create your models here.

# Indicador 13 -  Ingreso Familiar. Venta de rubros (periodo de referencia de mayo 2009 a abril 2010)

CHOICE_VENDIO = ((1,"Comunidad"),(2,"Intermediario"),(3,"Mercado"),
                 (4,"Cooperativa"),(5,'todos'))

CHOICE_MANEJA = ((1,"Hombre"),(2,"Mujer"),(3,"Ambos"),(4,"Hijos/as"),
                 (5,'Hombre-Hijos'),(6,'Mujer-Hijos'),(7,'Todos'))
                 
CHOICE_CATEG = (
                 (1,"Agroforestales"),
                 (2,"Forestales"),
                 (3,"Granos básicos"),
                 (4,"Ganado mayor"),
                 (5,"Animales de patio"),
                 (6,"Hortalizas y frutas"),
                 (7,"Musaceas"),
                 (8,"Raíces y tubérculos")
                     
                )

class Rubros(models.Model):
    nombre = models.CharField(max_length=50)
    unidad = models.CharField(max_length=50)
    categoria = models.IntegerField(choices=CHOICE_CATEG, null = True, blank = True)
    
    def __unicode__(self):
        return u'%s - %s' % (self.nombre,self.unidad)
        
    class Meta:
        verbose_name_plural = "IngresoFamiliar-Rubros"
        ordering = ['nombre']
        #app_label = "Indicador 13 Ingreso Familiar"
        #db_table = "simas_rubros"

class IngresoFamiliar(models.Model):
    ''' Modelo Ingreso familiar. venta de rubros
    '''
    rubro = models.ForeignKey(Rubros)
    cantidad = models.FloatField('Cantidad vendida en el año pasado',null=True, blank=True)
    precio = models.FloatField('Precio de venta por unidad',null=True, blank=True)
    quien_vendio = models.IntegerField('¿A quien vendio?', choices=CHOICE_VENDIO,null=True, blank=True)
    maneja_negocio = models.IntegerField('¿Quién maneja el negocio', choices=CHOICE_MANEJA,null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.rubro.nombre
    
    class Meta:
        verbose_name_plural = "Ingreso Familiar"
        #app_label = "Indicador 13 Ingreso Familiar"
        #db_table = "simas_ingresofamiliar"

#-------------------------------------------------------------------------------
