# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.simas.models import *

# Create your models here.

# Indicador 2. Organizacion gremial

class OrgGremiales(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Organizaciones Gremiales"

class BeneficiosObtenido(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Benificios Obtenidos"

class SerMiembro(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Porque quiere ser miembro"

CHOICE_DESDE = ((1,'Menos de 5 años'),(2,'Más de 5 años'),(3, 'No utilizar'))
CHOICE_MIEMBRO_GREMIAL = ((1,'Junta directiva'),(2,'No'),(3,'Comisiones de trabajo'))


class OrganizacionGremial(models.Model):
    ''' 2. Organizacion Gremial
    '''
    socio = models.ManyToManyField(OrgGremiales,
                                   verbose_name="Es socio/a de una organización gremial")
    desde_socio = models.IntegerField('Desde cuando', choices=CHOICE_DESDE)
    beneficio = models.ManyToManyField(BeneficiosObtenido,
                                       verbose_name="¿Qué beneficios ha tenido por ser socio/a de la cooperativa, la asociación o empresa")
    miembro_gremial = models.IntegerField('Soy miembro de órgano gremial',
                                          choices=CHOICE_MIEMBRO_GREMIAL)
    desde_miembro = models.IntegerField('Desde cuando', choices=CHOICE_DESDE)
    capacitacion = models.IntegerField('He recibido capacitación para desempeñar mi cargo',
                                      choices=CHOICE_OPCION)
    desde_capacitacion = models.IntegerField('Desde cuando', choices=CHOICE_DESDE)
    miembro_junta = models.ManyToManyField(SerMiembro,
                                           verbose_name="Porque soy o quiero ser miembro de la junta directiva o las comisiones")
    asumir_cargo = models.IntegerField('Si no es miembro de ninguna estructura, ¿estaria interesado en asumir un cargo', choices=CHOICE_OPCION)
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Organizacion Gremial"

# 2.1 Organización comunitaria

class OrgComunitarias(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Organizaciones comunitarias"

class BeneficioOrgComunitaria(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Beneficios de estar organizado en comunidad"
     
class NoOrganizado(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Porque No esta organizado"


class OrganizacionComunitaria(models.Model):
    ''' 2.1 Organizacion comunitarias
    '''
    numero = models.IntegerField('¿Cuántas organizaciones están activas en la localidad o comunidad')
    pertence = models.IntegerField('¿Pertenece a algunas organizaciones?', choices=CHOICE_OPCION)
    cual_organizacion = models.ManyToManyField(OrgComunitarias, verbose_name="¿A cuál organización comunitaria pertenece?")
    cual_beneficio = models.ManyToManyField(BeneficioOrgComunitaria, verbose_name="¿Cuáles son los beneficios de estar organizado")
    no_organizado = models.ManyToManyField(NoOrganizado, verbose_name="¿Porqué no esta organizado?")
    encuesta = models.ForeignKey(Encuesta)
    
    class Meta:
        verbose_name_plural = "Organizacion Comunitaria"

#-------------------------------------------------------------------------------

#UPDATE indicador02_organizaciongremial SET miembro_gremial = 1 WHERE miembro_gremial = 2;
