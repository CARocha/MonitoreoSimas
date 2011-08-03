# -*- coding: utf-8 -*-

from django.db import models
from monitoreo.simas.models import *

# Create your models here.

# Indicador 15. Propiedades y Bienes

CHOICE_AMBIENTE = ((1,"1"),(2,"2"),(3,"3"),(4,"4"),(5,"5"))
CHOICE_TIPO_CASA = ((1,"Madera rolliza"),(2,"Adobe"),(3,"Tabla"),
                    (4,"Minifalda"),(5,"Ladrillo o Bloque"))

class Piso(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Pisos"
        #app_label = "Indicador 15 Propiedades y Bienes"
        #db_table = "simas_piso"

class Techo(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Techos"
        #app_label = "Indicador 15 Propiedades y Bienes"
        #db_table = "simas_techo"

class TipoCasa(models.Model):
    '''Modelo tipos de casa
    '''
    tipo = models.IntegerField('Tipo de la casa', choices=CHOICE_TIPO_CASA)
    piso = models.ManyToManyField(Piso, verbose_name="Piso")
    techo = models.ManyToManyField(Techo, verbose_name="Techo")
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.get_tipo_display()

    class Meta:
        verbose_name_plural = "Tipos de Casas"
        #app_label = "Indicador 15 Propiedades y Bienes"
        #db_table = "simas_tipocasa"

CHOICE_AMBIENTE = ((1,"1"),(2,"2"),(3,"3"),(4,"4"),(5,"5"))

class DetalleCasa(models.Model):
    '''Modelo detalle de casa
    '''
    tamano = models.IntegerField('Tamaño en mt cuadrado',null=True, blank=True)
    ambientes = models.IntegerField(choices=CHOICE_AMBIENTE,null=True, blank=True)
    letrina = models.IntegerField(choices=CHOICE_OPCION,null=True, blank=True)
    lavadero = models.IntegerField(choices=CHOICE_OPCION,null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % str(self.tamano)

    class Meta:
        verbose_name_plural = "Detalle casa"
        #app_label = "Indicador 15 Propiedades y Bienes"
        #db_table = "simas_detallecasa"

class Equipos(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Propiedades-Equipos"
        #app_label = "Indicador 15 Propiedades y Bienes"
        #db_table = "simas_equipos"


class Infraestructuras(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Propiedades-Infraestructura"
        #app_label = "Indicador 15 Propiedades y Bienes"
        #db_table = "simas_infraestructuras"

class Propiedades(models.Model):
    '''Modelo propiedades
    '''
    equipo = models.ForeignKey(Equipos, null=True, blank=True)
    cantidad_equipo = models.IntegerField(null=True, blank=True)
    infraestructura = models.ForeignKey(Infraestructuras, null=True, blank=True)
    cantidad_infra = models.IntegerField('Cantidad', null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    #def __unicode__(self):
    #    return self.equipo.nombre
    
    class Meta:
        verbose_name_plural = "Propiedades"
        #app_label = "Indicador 15 Propiedades y Bienes"
        #db_table = "simas_propiedades"


class NombreHerramienta(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Herramientas-Nombres"
        #app_label = "Indicador 15 Propiedades y Bienes"
        #db_table = "simas_nombreherramienta"


class Herramientas(models.Model):
    '''Modelo herramientas
    '''
    herramienta = models.ForeignKey(NombreHerramienta)
    numero = models.IntegerField(null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)

    def __unicode__(self):
        return self.herramienta.nombre

    class Meta:
        verbose_name_plural = "Herramientas"
        #app_label = "Indicador 15 Propiedades y Bienes"
        #db_table = "simas_herramienta"


class NombreTransporte(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Transporte-Nombre"
        #app_label = "Indicador 15 Propiedades y Bienes"
        #db_table = "simas_nombretransporte"


class Transporte(models.Model):
    '''Modelo transporte
    '''
    transporte = models.ForeignKey(NombreTransporte)
    numero = models.IntegerField(null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.transporte.nombre
    
    class Meta:
        verbose_name_plural = "Transporte"
        #app_label = "Indicador 15 Propiedades y Bienes"
        #db_table = "simas_transporte"

#-------------------------------------------------------------------------------
