# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.simas.models import *

# Create your models here.

# Indicador 1: Familia

CHOICE_EDUCACION = ((1,'Hombre mas de 18 años'),(2,'Mujeres mas de 18 años'),(3,'Hombre de 7 a 18 años'),
                     (4,'Mujeres de 7 a 18 años'),(5,'Niños menos de 6 años'),(6,'Niñas menos de 6 años'))

class Educacion(models.Model):
    ''' 1.1 - composicion y educacion
    '''
    sexo = models.IntegerField(choices=CHOICE_EDUCACION)
    total = models.IntegerField('Número total')
    no_leer = models.IntegerField('No sabe leer y escribir')
    p_incompleta = models.IntegerField('Primaria incompleta')
    p_completa = models.IntegerField('Primaria completa')
    s_incompleta = models.IntegerField('Secundaria incompleta')
    bachiller = models.IntegerField()
    universitario = models.IntegerField()
    f_comunidad = models.IntegerField('Viven fuera de la comunidad')
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.get_sexo_display()
        
    class Meta:
        verbose_name_plural = "Educacion"
        #app_label = " Indicador 01 Educacion"
        #db_table = "simas_educacion"

#-------------------------------------------------------------------------------

CHOICE_SALUD = ((1,'Si'),(2,'No'),(3,'No sabe'))

class Salud(models.Model):
    ''' 1.2 salud
    '''
    sexo = models.IntegerField(choices=CHOICE_EDUCACION)
    b_salud = models.IntegerField('# tiene buena salud')
    s_delicada = models.IntegerField('# tiene salud delicada')
    e_cronica = models.IntegerField('# tiene enfermedad crónica')
    v_centro = models.IntegerField('Visita centro de salud', choices=CHOICE_SALUD)
    v_medico = models.IntegerField('Visita médico privado', choices=CHOICE_SALUD)
    v_naturista = models.IntegerField('Visita médico naturista', choices=CHOICE_SALUD)
    automedica = models.IntegerField('Se automedica', choices=CHOICE_SALUD)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.get_sexo_display()
        
    class Meta:
        verbose_name_plural = "Salud"
        #app_label = "Indicador 01 Salud"
        #db_table = "simas_salud"

#-------------------------------------------------------------------------------

class PreguntaEnergia(models.Model):
    pregunta = models.CharField(max_length=200)

    def __unicode__(self):
        return self.pregunta

    class Meta:
        verbose_name_plural = "Pregunta sobre energia"
        #app_label = "Indicador 01 Energia"
        #db_table = "simas_preguntaenergia"

class Energia(models.Model):
    ''' 1.3 energia
    '''
    pregunta = models.ForeignKey(PreguntaEnergia)
    respuesta = models.IntegerField(choices=CHOICE_OPCION)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Energia"
        #app_label = "Indicador 01 Energia"
        #db_table = "simas_energia"

class TipoCocina(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Utiliza para cocinar"
class Cocina(models.Model):
    ''' Que utiliza para cocinar
    '''
    utiliza = models.ManyToManyField(TipoCocina, verbose_name="Qué utiliza para cocinar", null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
#-------------------------------------------------------------------------------

class Fuente(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Fuentes de consumo de agua"
        #app_label = "Indicador 01 Agua"
        #db_table = "simas_fuente"

class Tratamiento(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tratamiento de agua de consumo"
        #app_label = "Indicador 01 Agua"
        #db_table = "simas_tratamiento"

class Disponibilidad(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Disponibilidad de agua para consumo"
        #app_label = "Indicador 01 Agua"
        #db_table = "simas_disponibilidad"

class Agua(models.Model):
    ''' 1.4 Agua de consumo
    '''
    fuente = models.ManyToManyField(Fuente, verbose_name="Fuente de consumo de agua")
    trata = models.ManyToManyField(Tratamiento, verbose_name="¿Cómo se trata el agua para consumo")
    disponible = models.ManyToManyField(Disponibilidad, verbose_name="Disponibilidad de agua para consumo")
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Agua"
        #app_label = "Indicador 01 Agua"
        #db_table = "simas_agua"

#-------------------------------------------------------------------------------
