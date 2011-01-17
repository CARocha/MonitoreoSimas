# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.simas.models import *

# Create your models here.

# Indicador 12. Suelo

class Textura(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Suelo - Textura"
        #app_label = "Indicador 12 Suelo"
        #db_table = "simas_textura"

class Profundidad(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Suelo - Profundidad"
        #app_label = "Indicador 12 Suelo"
        #db_table = "simas_profundidad"

# Esta clase de va a ocupar en varias de los tipos de caraterización
# ya que contendra las opciones Alta, Media y Baja
class Densidad(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Suelo - Densidad"
        #app_label = "Indicador 12 Suelo"
        #db_table = "simas_densidad"

class Pendiente(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Suelo - Pendiente"
        #app_label = "Indicador 12 Suelo"
        #db_table = "simas_pendiente"

class Drenaje(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Suelo - Drenaje"
        #app_label = "Indicador 12 Suelo"
        #db_table = "simas_drenaje"

class Suelo(models.Model):
    ''' 12.1 - Caracterización de terreno
    '''
    textura = models.ManyToManyField(Textura,
                                     verbose_name="¿Cúal es el tipo de textura del suelo?")
    profundidad = models.ManyToManyField(Profundidad,
                                         verbose_name="¿Cúal es la profundidad del suelo?")
    lombrices = models.ManyToManyField(Densidad,
                                       verbose_name="¿Cómo es la presencia de lombrice en el suelo?",
                                       related_name="lombrices")
    densidad = models.ManyToManyField(Densidad,
                                      verbose_name="¿Cómo es la densidad de raiz en la capa productiva de suelo?",
                                      related_name="densidad")
    pendiente = models.ManyToManyField(Pendiente,
                                       verbose_name="¿Cúal es la pendiente del terrreno?")
    drenaje = models.ManyToManyField(Drenaje,
                                     verbose_name="¿Cómo es el drenaje del suelo?")
    materia = models.ManyToManyField(Densidad,
                                     verbose_name="Cómo en el contenido de materia orgánica",
                                     related_name="materia")
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Suelo"
        #app_label = "Indicador 12 Suelo"
        #db_table = "simas_suelo"

# 12.2 Manejo de suelo

class Preparar(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "ManejoSuelo - preparar"
        #app_label = "Indicador 12 Suelo"
        #db_table = "simas_preparar"

class Traccion(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "ManejoSuelo - tracción"
        #app_label = "Indicador 12 Suelo"
        #db_table = "simas_traccion"

class Fertilizacion(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "ManejoSuelo - fertilizacion"
        #app_label = "Indicador 12 Suelo"
        #db_table = "simas_fertilizacion"

class Conservacion(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "ManejoSuelo - conservacion"
        #app_label = "Indicador 12 Suelo"
        #db_table = "simas_conservacion"

class ManejoSuelo(models.Model):
    ''' 12.2 Manejo de suelo
    '''
    preparan = models.ManyToManyField(Preparar, verbose_name="¿Cómo preparan sus terrenos?")
    traccion = models.ManyToManyField(Traccion,
                                      verbose_name="¿Qué tipo de traccion utiliza para la preparación del suelo?")
    analisis = models.IntegerField('¿Realiza análisis de fertilidad del suelo', choices=CHOICE_OPCION)
    fertilizacion = models.ManyToManyField(Fertilizacion, verbose_name="¿Qué tipo de fertilización realiza?")
    practica = models.IntegerField('¿Realiza práctica de conservación de suelo', choices=CHOICE_OPCION)
    obra = models.ManyToManyField(Conservacion, verbose_name="¿Qué tipo de obra de conservación de suelo?")
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Manejo de Suelo"
        #app_label = "Indicador 12 Suelo"
        #db_table = "simas_manejosuelo"

#-------------------------------------------------------------------------------
