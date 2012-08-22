# -*- coding: utf-8 -*-

from django.db import models
from thumbs import ImageWithThumbsField
from monitoreo.lugar.models import Comunidad, Departamento, Municipio
from django.conf import settings
from monitoreo.utils import get_file_path 
from django.contrib.auth.models import User

# Create your models here.
class Recolector(models.Model):
    ''' Esta es la clase para el nombre del recolector
    '''
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Recolector"

CHOICE_ZONA = ((1,'Seca'),(2,'Alta'))

class Organizaciones(models.Model):
    nombre = models.CharField(max_length=200)
    telefono = models.IntegerField(null=True, blank=True)
    fax = models.IntegerField(null=True, blank=True)
    celular = models.IntegerField(null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    correo_electronico = models.EmailField(null=True, blank=True)
    departamento = models.ForeignKey(Departamento, null=True, blank=True)
    logo = ImageWithThumbsField(upload_to=get_file_path, 
                                sizes=((150,150),(250,250)), null=True, blank=True)
    sitio_web = models.URLField(null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    zona = models.IntegerField(choices=CHOICE_ZONA)
    fileDir = 'attachments/logos'

    def __unicode__(self):
        return self.nombre
#        return '%s - %s' % (self.departamento.nombre, self.nombre)

    class Meta:
        verbose_name_plural = "Organizaciones"

CHOICE_SEXO = ((1,'Hombre'),(2,'Mujer'))
CHOICE_OPCION = ((1,'Si'),(2,'No')) # Este choice se utilizara en toda la aplicacion que necesite si o no

class Encuesta(models.Model):
    ''' Esta es la parte de la encuesta donde van los demas
    '''
    fecha = models.DateField()
    recolector = models.ForeignKey(Recolector)
    nombre = models.CharField('Nombre de entrevistado/a', max_length=200)
    cedula = models.CharField('cedula de entrevistado', max_length=200, null=True, blank=True)
    finca = models.CharField('Nombre de Finca', max_length=200)
    comunidad = models.ForeignKey(Comunidad)
    sexo = models.IntegerField(choices=CHOICE_SEXO)
    organizacion = models.ManyToManyField(Organizaciones, related_name ="org")
    user = models.ForeignKey(User)
    
    #campos ocultos para querys
    year = models.IntegerField(editable=False)
    
    def save(self):
        self.year = self.fecha.year
        super(Encuesta, self).save()
    
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Encuesta"

## Indicador 1: Familia

CHOICE_EDUCACION = ((1,'Hombre mas de 18 años'),(2,'Mujeres mas de 18 años'),(3,'Hombre de 7 a 18 años'),
                     (4,'Mujeres de 7 a 18 años'),(5,'Niños menos de 6 años'),(6,'Niñas menos de 6 años'))

#class Educacion(models.Model):
#    ''' 1.1 - composicion y educacion
#    '''
#    sexo = models.IntegerField(choices=CHOICE_EDUCACION)
#    total = models.IntegerField('Número total')
#    no_leer = models.IntegerField('No sabe leer y escribir')
#    p_incompleta = models.IntegerField('Primaria incompleta')
#    p_completa = models.IntegerField('Primaria completa')
#    s_incompleta = models.IntegerField('Secundaria incompleta')
#    bachiller = models.IntegerField()
#    universitario = models.IntegerField()
#    f_comunidad = models.IntegerField('Viven fuera de la comunidad')
#    encuesta = models.ForeignKey(Encuesta)
#    
#    def __unicode__(self):
#        return u'%s' % self.get_sexo_display()
#        
#    class Meta:
#        verbose_name_plural = "Educacion"
#        #app_label = " Indicador 01 Educacion"
#        #db_table = "simas_educacion"

##-------------------------------------------------------------------------------

#CHOICE_SALUD = ((1,'Si'),(2,'No'),(3,'No sabe'))

#class Salud(models.Model):
#    ''' 1.2 salud
#    '''
#    sexo = models.IntegerField(choices=CHOICE_EDUCACION)
#    b_salud = models.IntegerField('# tiene buena salud')
#    s_delicada = models.IntegerField('# tiene salud delicada')
#    e_cronica = models.IntegerField('# tiene enfermedad crónica')
#    v_centro = models.IntegerField('Visita centro de salud', choices=CHOICE_SALUD)
#    v_medico = models.IntegerField('Visita médico privado', choices=CHOICE_SALUD)
#    v_naturista = models.IntegerField('Visita médico naturista', choices=CHOICE_SALUD)
#    automedica = models.IntegerField('Se automedica', choices=CHOICE_SALUD)
#    encuesta = models.ForeignKey(Encuesta)
#    
#    def __unicode__(self):
#        return u'%s' % self.get_sexo_display()
#        
#    class Meta:
#        verbose_name_plural = "Salud"
#        #app_label = "Indicador 01 Salud"
#        #db_table = "simas_salud"

##-------------------------------------------------------------------------------

#class PreguntaEnergia(models.Model):
#    pregunta = models.CharField(max_length=200)

#    def __unicode__(self):
#        return self.pregunta

#    class Meta:
#        verbose_name_plural = "Pregunta sobre energia"
#        #app_label = "Indicador 01 Energia"
#        #db_table = "simas_preguntaenergia"

#class Energia(models.Model):
#    ''' 1.3 energia
#    '''
#    pregunta = models.ForeignKey(PreguntaEnergia)
#    respuesta = models.IntegerField(choices=CHOICE_OPCION)
#    encuesta = models.ForeignKey(Encuesta)
#    
#    class Meta:
#        verbose_name_plural = "Energia"
#        #app_label = "Indicador 01 Energia"
#        #db_table = "simas_energia"

##-------------------------------------------------------------------------------

#class Fuente(models.Model):
#    nombre = models.CharField(max_length=200)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Fuentes de consumo de agua"
#        #app_label = "Indicador 01 Agua"
#        #db_table = "simas_fuente"

#class Tratamiento(models.Model):
#    nombre = models.CharField(max_length=200)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Tratamiento de agua de consumo"
#        #app_label = "Indicador 01 Agua"
#        #db_table = "simas_tratamiento"

#class Disponibilidad(models.Model):
#    nombre = models.CharField(max_length=200)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Disponibilidad de agua para consumo"
#        #app_label = "Indicador 01 Agua"
#        #db_table = "simas_disponibilidad"

#class Agua(models.Model):
#    ''' 1.4 Agua de consumo
#    '''
#    fuente = models.ManyToManyField(Fuente, verbose_name="Fuente de consumo de agua")
#    trata = models.ManyToManyField(Tratamiento, verbose_name="¿Cómo se trata el agua para consumo")
#    disponible = models.ManyToManyField(Disponibilidad, verbose_name="Disponibilidad de agua para consumo")
#    encuesta = models.ForeignKey(Encuesta)
#    
#    class Meta:
#        verbose_name_plural = "Agua"
#        #app_label = "Indicador 01 Agua"
#        #db_table = "simas_agua"

##------------------------------------------------------------------------------

## Indicador 2. Organizacion gremial

#class OrgGremiales(models.Model):
#    nombre = models.CharField(max_length=200)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Organizaciones Gremiales"
#        #app_label = "Indicador 02 Organizacion Gremial"
#        #db_table = "simas_orggremial"

#class BeneficiosObtenido(models.Model):
#    nombre = models.CharField(max_length=200)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Benificios Obtenidos"
#        #app_label = "Indicador 02 Organizacion Gremial"
#        #db_table = "simas_beneficiosobtenidos"

#class SerMiembro(models.Model):
#    nombre = models.CharField(max_length=200)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Porque quiere ser miembro"
#        #app_label = "Indicador 02 Organizacion Gremial"
#        #db_table = "simas_sermiembro"

CHOICE_DESDE = ((1,'Menos de 5 años'),(2,'Más de 5 años'),(3,'No utilizar'))
#CHOICE_MIEMBRO_GREMIAL = ((1,'Junta directiva'),(2,'Comisiones de trabajo'),(3,'No'))


#class OrganizacionGremial(models.Model):
#    ''' 2. Organizacion Gremial
#    '''
#    socio = models.ManyToManyField(OrgGremiales,
#                                   verbose_name="Es socio/a de una organización gremial")
#    desde_socio = models.IntegerField('Desde cuando', choices=CHOICE_DESDE)
#    beneficio = models.ManyToManyField(BeneficiosObtenido,
#                                       verbose_name="¿Qué beneficios ha tenido por ser socio/a de la cooperativa, la asociación o empresa")
#    miembro_gremial = models.IntegerField('Soy miembro de órgano gremial',
#                                          choices=CHOICE_MIEMBRO_GREMIAL)
#    desde_miembro = models.IntegerField('Desde cuando', choices=CHOICE_DESDE)
#    capacitacion = models.IntegerField('He recibido capacitación para desempeñar mi cargo',
#                                      choices=CHOICE_OPCION)
#    desde_capacitacion = models.IntegerField('Desde cuando', choices=CHOICE_DESDE)
#    miembro_junta = models.ManyToManyField(SerMiembro,
#                                           verbose_name="Porque soy o quiero ser miembro de la junta directiva o las comisiones")
#    asumir_cargo = models.IntegerField('Si no es miembro de ninguna estructura, ¿estaria interesado en asumir un cargo', choices=CHOICE_OPCION)
#    encuesta = models.ForeignKey(Encuesta)
#    
#    class Meta:
#        verbose_name_plural = "Organizacion Gremial"
#        #app_label = "Indicador 02 Organizacion Gremial"
#        #db_table = "simas_organizaciongremial"

## 2.1 Organización comunitaria

#class OrgComunitarias(models.Model):
#    nombre = models.CharField(max_length=200)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Organizaciones comunitarias"
#        #app_label = "Indicador 02 Organizacion Comunitaria"
#        #db_table = "simas_orgcomunitarias"

#class BeneficioOrgComunitaria(models.Model):
#    nombre = models.CharField(max_length=200)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Beneficios de estar organizado en comunidad"
#        #app_label = "Indicador 02 Organizacion Comunitaria"
#        #db_table = "simas_beneficiorgcomunitaria"

#class NoOrganizado(models.Model):
#    nombre = models.CharField(max_length=200)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Porque No esta organizado"
#        #app_label = "Indicador 02 Organizacion Comunitaria"
#        #db_table = "simas_noorganizado"


#class OrganizacionComunitaria(models.Model):
#    ''' 2.1 Organizacion comunitarias
#    '''
#    numero = models.IntegerField('¿Cuántas organizaciones están activas en la localidad o comunidad')
#    pertence = models.IntegerField('¿Pertenece a algunas organizaciones?', choices=CHOICE_OPCION)
#    cual_organizacion = models.ManyToManyField(OrgComunitarias, verbose_name="¿A cuál organización comunitaria pertenece?")
#    cual_beneficio = models.ManyToManyField(BeneficioOrgComunitaria, verbose_name="¿Cuáles son los beneficios de estar organizado")
#    no_organizado = models.ManyToManyField(NoOrganizado, verbose_name="¿Porqué no esta organizado?")
#    encuesta = models.ForeignKey(Encuesta)
#    
#    class Meta:
#        verbose_name_plural = "Organizacion Comunitaria"
#        #app_label = "Indicador 02 Organizacion Comunitaria"
#        #db_table = "simas_organizacioncomunitaria"

##-------------------------------------------------------------------------------

# Indicador 3 y 4. Tipo de tenencia de parcela y solar y Documento legal de la propiedad, a nombre de quién

CHOICE_TENENCIA = ((1,"Propia con escritura pública"),(2,"Propia por herencia"),
                   (3,"Propias con promesa de venta"),(4,"Propias con titulo de reforma agraria"),
                   (5,"Arrendada"),(6,"Sin documento"),(7,"Escritura posesoria"),(8,"No tiene"))
                   
                   
CHOICE_DUENO = ((1,"Hombre"),(2,"Mujer"),(3,"Mancomunado"),(4,"Parientes"),
                (5,"Colectivo"),(6,"No hay"))

class Tenencia(models.Model):
    ''' Modelo tipo de tenencia de la propiedad
    '''
    parcela = models.IntegerField('Parcela (tierra)', choices=CHOICE_TENENCIA)
    solar = models.IntegerField('Solar (dónde está la vivienda)', choices=CHOICE_TENENCIA)
    dueno = models.IntegerField('Documento legal de la propiedad, a nombre de quien', choices=CHOICE_DUENO)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.get_parcela_display()

#-------------------------------------------------------------------------------

## Indicador 5 Uso de Tierrra

#class Uso(models.Model):
#    nombre = models.CharField(max_length=200)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Uso de tierra"
#        #app_label = "Indicador 05 Uso de Tierra"
#        #db_table = "simas_uso"

#class UsoTierra(models.Model):
#    ''' Uso de tierra
#    '''
#    tierra = models.ForeignKey(Uso, verbose_name="Uso de Tierra")
#    area = models.FloatField('Área en Mz')
#    encuesta = models.ForeignKey(Encuesta)
#    
#    def __unicode__(self):
#        return u'%s' % self.tierra.nombre

#-------------------------------------------------------------------------------

# Indicador 6. Existencia de arboles en la finca por tipo de uso

#class Maderable(models.Model):
#    nombre = models.CharField(max_length=200)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Arboles maderables"
#        #app_label = "Indicador 06 existencia de arboles"
#        #db_table = "simas_maderable"

#class Forrajero(models.Model):
#    nombre = models.CharField(max_length=200)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Arboles forrageros"
#        #app_label = "Indicador 06 existencia de arboles"
#        #db_table = "simas_forrajero"

#class Energetico(models.Model):
#    nombre = models.CharField(max_length=200)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Arboles energeticos"
#        #app_label = "Indicador 06 existencia de arboles"
#        #db_table = "simas_energetico"

#class Frutal(models.Model):
#    nombre = models.CharField(max_length=200)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Arboles frutal"
#        #app_label = "Indicador 06 existencia de arboles"
#        #db_table = "simas_frutal"

#class ExistenciaArboles(models.Model):
#    ''' Existencia de arboles en la finca
#        por tipo de uso
#    '''
#    maderable = models.ManyToManyField(Maderable, verbose_name="Maderable")
#    cantidad_maderable = models.IntegerField()
#    forrajero = models.ManyToManyField(Forrajero, verbose_name="Forrajero")
#    cantidad_forrajero = models.IntegerField()
#    energetico = models.ManyToManyField(Energetico, verbose_name="Energetico")
#    cantidad_energetico = models.IntegerField()
#    frutal = models.ManyToManyField(Frutal, verbose_name="Frutal")
#    cantidad_frutal = models.IntegerField()
#    encuesta = models.ForeignKey(Encuesta)
#    
#    class Meta:
#        verbose_name_plural = " Existencia de Arboles"
#        #app_label = "Indicador 06 existencia de arboles"
#        #db_table = "simas_existenciaarboles"

##-------------------------------------------------------------------------------

# Indicador 7. Reforestación (periodo de referencia de mayo 2009 a abril 2010)

#class Actividad(models.Model):
#    nombre = models.CharField(max_length=200)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Actividades de reforestacion"
#        #app_label = "Indicador 07 Reforestacion"
#        #db_table = "simas_actividad"

#class Reforestacion(models.Model):
#    ''' reforestacion
#    '''
#    reforestacion = models.ForeignKey(Actividad, verbose_name="Actividades de reforestación")
#    cantidad = models.IntegerField('Cantidad de arboles sembrados')
#    encuesta = models.ForeignKey(Encuesta)
#    
#    def __unicode__(self):
#        return u'%s' % self.reforestacion.nombre
#    
#    class Meta:
#        verbose_name_plural = "Reforestacion"
        #app_label = "Indicador 07 Reforestacion"
        #db_table = "simas_reforestacion"

#-------------------------------------------------------------------------------

# Indicador 8. Animales en la finca y la producción (periodo de referencia de mayo 2009 a abril 2010)

#class Animales(models.Model):
#    nombre = models.CharField(max_length=50)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Finca - Animales"
#        #app_label = "Indicador 08 Produccion y animales en la finca"
#        #db_table = "simas_animales"

#class ProductoAnimal(models.Model):
#    nombre = models.CharField(max_length=100)
#    unidad = models.CharField(max_length=100)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Finca - Producto"
        #app_label = "Indicador 08 Produccion y animales en la finca"
        #db_table = "simas_productoanimal"


#class AnimalesFinca(models.Model):
#    ''' Modelo animales en la finca
#    '''
#    animales = models.ForeignKey(Animales)
#    cantidad = models.FloatField()
#    produccion = models.ForeignKey(ProductoAnimal)
#    total_produccion = models.IntegerField('Total producion por año', null=True)
#    consumo = models.FloatField('Consumo')
#    venta_libre = models.FloatField('Venta libre')
#    venta_organizada = models.FloatField('Venta organizada')
#    encuesta = models.ForeignKey(Encuesta)
#    
#    def __unicode__(self):
#        return u'%s' % self.animales.nombre
#    
#    class Meta:
#        verbose_name_plural = "Animales en la finca"
        #app_label = "Indicador 08 Produccion y animales en la finca"
        #db_table = "simas_animalesfinca"

#-------------------------------------------------------------------------------

# Indicador 9. Cultivos en la finca (periodo de referencia de mayo 2009 a abril 2010)

#class Cultivos(models.Model):
#    nombre = models.CharField(max_length=50)
#    unidad = models.CharField(max_length=50)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "CultivosFinca-Cultivos"
#        #app_label = "Indicador 09 cultivos en la finca"
#        #db_table = "simas_cultivos"


#class CultivosFinca(models.Model):
#    ''' indicador cultivos en la finca
#    '''
#    cultivos = models.ForeignKey(Cultivos)
#    area =  models.FloatField('Área/Mz')
#    total = models.FloatField('Total producción por año')
#    consumo = models.FloatField('Consumo por año')
#    venta_libre = models.FloatField('Venta libre por año')
#    venta_organizada = models.FloatField('Venta organizada por año')
#    encuesta = models.ForeignKey(Encuesta)
#    
#    def __unicode__(self):
#        return u'%s' % self.cultivos.nombre
#    
#    class Meta:
#        verbose_name_plural = "Cultivos en la finca"
        #app_label = "Indicador 09 cultivos en la finca"
        #db_table = "simas_cultivosfinca"

#-------------------------------------------------------------------------------

# Indicador 10. Opciones de manejo agroecologico

#class ManejoAgro(models.Model):
#    nombre = models.CharField(max_length=50)
#    unidad = models.CharField(max_length=50)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Uso opciones de manejo agroecologico"
#        #app_label = "Indicador 10 Opciones de manejo agroecologico"
#        #db_table = "simas_manejoagro"

#CHOICE_NIVEL_CONOCIMIENTO = ((1,'Nada'),(2,'Poco'),(3,'Algo'),(4,'Bastante'))

#class OpcionesManejo(models.Model):
#    ''' opciones de manejo agroecologico
#    '''
#    uso = models.ForeignKey(ManejoAgro, verbose_name="Uso de opciones de manejo agroecologico")
#    nivel = models.IntegerField('Nivel de conocimiento', choices=CHOICE_NIVEL_CONOCIMIENTO)
#    menor_escala = models.IntegerField('Han experimentado en pequeña escala', choices=CHOICE_OPCION)
#    mayor_escala = models.IntegerField('Han experimentado en mayor escala', choices=CHOICE_OPCION)
#    volumen = models.FloatField('¿Qué área, número o volumen')
#    encuesta = models.ForeignKey(Encuesta)
#    
#    def __unicode__(self):
#        return u'%s' % self.uso.nombre
#    
#    class Meta:
#        verbose_name_plural = "Opciones de manejo"
        #app_label = "Indicador 10 Opciones de manejo agroecologico"
        #db_table = "simas_opcionesmanejo"

#-------------------------------------------------------------------------------

# Indicador 11. uso de semilla

#class CultivosVariedad(models.Model):
#    cultivo = models.CharField(max_length=200)

#    def __unicode__(self):
#        return self.cultivo

#    class Meta:
#        verbose_name_plural = "Cultivos variedad"
        #app_label = "Indicador 11 Uso de semilla"
        #db_table = "simas_cultivosvariedad"

#class Variedades(models.Model):
#    cultivo = models.ForeignKey(CultivosVariedad)
#    variedad = models.CharField(max_length=200)

#    def __unicode__(self):
#        return '%s - %s' % (self.cultivo.cultivo, self.variedad)

#    class Meta:
#        verbose_name_plural = "Variedades"
#        #app_label = "Indicador 11 Uso de semilla"
#        #db_table = "simas_variedades"

#CHOICE_ORIGEN = ((1,'Nativo'), (2,'Introducido'))

#class Semilla(models.Model):
#    ''' uso de semilla
#    '''
#    cultivo = models.ForeignKey(Variedades, verbose_name="cultivo y su variedad",
#                                help_text="Escoja el cultivo con su variedad")
#    origen = models.IntegerField('Origen', choices=CHOICE_ORIGEN)
#    encuesta = models.ForeignKey(Encuesta)
#    
#    def __unicode__(self):
#        return u'%s' % self.cultivo.cultivo
#    
#    class Meta:
#        verbose_name_plural = "Semilla"
#        #app_label = "Indicador 11 Uso de semilla"
#        #db_table = "simas_semilla"

##-------------------------------------------------------------------------------

## Indicador 12. Suelo

#class Textura(models.Model):
#    nombre = models.CharField(max_length=200)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Suelo - Textura"
#        #app_label = "Indicador 12 Suelo"
#        #db_table = "simas_textura"

#class Profundidad(models.Model):
#    nombre = models.CharField(max_length=200)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Suelo - Profundidad"
#        #app_label = "Indicador 12 Suelo"
#        #db_table = "simas_profundidad"

## Esta clase de va a ocupar en varias de los tipos de caraterización
## ya que contendra las opciones Alta, Media y Baja
#class Densidad(models.Model):
#    nombre = models.CharField(max_length=200)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Suelo - Densidad"
#        #app_label = "Indicador 12 Suelo"
#        #db_table = "simas_densidad"

#class Pendiente(models.Model):
#    nombre = models.CharField(max_length=200)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Suelo - Pendiente"
#        #app_label = "Indicador 12 Suelo"
#        #db_table = "simas_pendiente"

#class Drenaje(models.Model):
#    nombre = models.CharField(max_length=200)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Suelo - Drenaje"
#        #app_label = "Indicador 12 Suelo"
#        #db_table = "simas_drenaje"

#class Suelo(models.Model):
#    ''' 12.1 - Caracterización de terreno
#    '''
#    textura = models.ManyToManyField(Textura,
#                                     verbose_name="¿Cúal es el tipo de textura del suelo?")
#    profundidad = models.ManyToManyField(Profundidad,
#                                         verbose_name="¿Cúal es la profundidad del suelo?")
#    lombrices = models.ManyToManyField(Densidad,
#                                       verbose_name="¿Cómo es la presencia de lombrice en el suelo?",
#                                       related_name="lombrices")
#    densidad = models.ManyToManyField(Densidad,
#                                      verbose_name="¿Cómo es la densidad de raiz en la capa productiva de suelo?",
#                                      related_name="densidad")
#    pendiente = models.ManyToManyField(Pendiente,
#                                       verbose_name="¿Cúal es la pendiente del terrreno?")
#    drenaje = models.ManyToManyField(Drenaje,
#                                     verbose_name="¿Cómo es el drenaje del suelo?")
#    materia = models.ManyToManyField(Densidad,
#                                     verbose_name="Cómo en el contenido de materia orgánica",
#                                     related_name="materia")
#    encuesta = models.ForeignKey(Encuesta)
#    
#    class Meta:
#        verbose_name_plural = "Suelo"
#        #app_label = "Indicador 12 Suelo"
#        #db_table = "simas_suelo"

## 12.2 Manejo de suelo

#class Preparar(models.Model):
#    nombre = models.CharField(max_length=200)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "ManejoSuelo - preparar"
#        #app_label = "Indicador 12 Suelo"
#        #db_table = "simas_preparar"

#class Traccion(models.Model):
#    nombre = models.CharField(max_length=200)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "ManejoSuelo - tracción"
#        #app_label = "Indicador 12 Suelo"
#        #db_table = "simas_traccion"

#class Fertilizacion(models.Model):
#    nombre = models.CharField(max_length=200)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "ManejoSuelo - fertilizacion"
#        #app_label = "Indicador 12 Suelo"
#        #db_table = "simas_fertilizacion"

#class Conservacion(models.Model):
#    nombre = models.CharField(max_length=200)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "ManejoSuelo - conservacion"
#        #app_label = "Indicador 12 Suelo"
#        #db_table = "simas_conservacion"

#class ManejoSuelo(models.Model):
#    ''' 12.2 Manejo de suelo
#    '''
#    preparan = models.ManyToManyField(Preparar, verbose_name="¿Cómo preparan sus terrenos?")
#    traccion = models.ManyToManyField(Traccion,
#                                      verbose_name="¿Qué tipo de traccion utiliza para la preparación del suelo?")
#    analisis = models.IntegerField('¿Realiza análisis de fertilidad del suelo', choices=CHOICE_OPCION)
#    fertilizacion = models.ManyToManyField(Fertilizacion, verbose_name="¿Qué tipo de fertilización realiza")
#    practica = models.IntegerField('¿Realiza práctica de conservación de suelo', choices=CHOICE_OPCION)
#    obra = models.ManyToManyField(Conservacion, verbose_name="¿Qué tipo de obra de conservación de suelo?")
#    encuesta = models.ForeignKey(Encuesta)
#    
#    class Meta:
#        verbose_name_plural = "Manejo de Suelo"
#        #app_label = "Indicador 12 Suelo"
#        #db_table = "simas_manejosuelo"

##-------------------------------------------------------------------------------

## Indicador 13 -  Ingreso Familiar. Venta de rubros (periodo de referencia de mayo 2009 a abril 2010)

#CHOICE_VENDIO = ((1,"Comunidad"),(2,"Intermediario"),(3,"Mercado"),
#                 (4,"Cooperativa"),(5,'todos'))

CHOICE_MANEJA = ((1,"Hombre"),(2,"Mujer"),(3,"Ambos"),(4,"Hijos/as"),
                 (5,'Hombre-Hijos'),(6,'Mujer-Hijos'),(7,'Todos'))

#class Rubros(models.Model):
#    nombre = models.CharField(max_length=50)
#    unidad = models.CharField(max_length=50)
#    
#    def __unicode__(self):
#        return self.nombre
#        
#    class Meta:
#        verbose_name_plural = "IngresoFamiliar-Rubros"
#        #app_label = "Indicador 13 Ingreso Familiar"
#        #db_table = "simas_rubros"

#class IngresoFamiliar(models.Model):
#    ''' Modelo Ingreso familiar. venta de rubros
#    '''
#    rubro = models.ForeignKey(Rubros)
#    cantidad = models.IntegerField('Cantidad vendida en el año pasado',null=True, blank=True)
#    precio = models.IntegerField('Precio de venta por unidad',null=True, blank=True)
#    quien_vendio = models.IntegerField('¿A quien vendio?', choices=CHOICE_VENDIO,null=True, blank=True)
#    maneja_negocio = models.IntegerField('¿Quién maneja el negocio', choices=CHOICE_MANEJA,null=True, blank=True)
#    encuesta = models.ForeignKey(Encuesta)
#    
#    def __unicode__(self):
#        return u'%s' % self.rubro.nombre
#    
#    class Meta:
#        verbose_name_plural = "Ingreso Familiar"
        #app_label = "Indicador 13 Ingreso Familiar"
        #db_table = "simas_ingresofamiliar"

#-------------------------------------------------------------------------------

# Indicador 14 Otros ingresos.

#class Fuentes(models.Model):
#    nombre = models.CharField(max_length=100)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Otros-Ingreso - Fuentes"
#        #app_label = "Indicador 14 Otros Ingresos"
#        #db_table = "simas_fuentes"

#class TipoTrabajo(models.Model):
#    nombre = models.CharField(max_length=200)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Otro-Ingreso - TipoTrabajo"
#        #app_label = "Indicador 14 Otros Ingresos"
#        #db_table = "simas_tipotrabajo"

#class OtrosIngresos(models.Model):
#    '''Otros ingresos
#    '''
#    fuente = models.ForeignKey(Fuentes)
#    tipo = models.ForeignKey(TipoTrabajo)
#    meses = models.IntegerField('# Meses',null=True, blank=True)
#    ingreso = models.IntegerField('Ingreso por mes',null=True, blank=True)
#    tiene_ingreso = models.IntegerField(choices=CHOICE_MANEJA,null=True, blank=True)
#    encuesta = models.ForeignKey(Encuesta)
#    
#    def __unicode__(self):
#        return u'%s' % self.fuente.nombre
#    
#    class Meta:
#        verbose_name_plural = "Otros Ingresos"
        #app_label = "Indicador 14 Otros Ingresos"
        #db_table = "simas_otrosingresos"

#-------------------------------------------------------------------------------

# Indicador 15. Propiedades y Bienes

#CHOICE_AMBIENTE = ((1,"1"),(2,"2"),(3,"3"),(4,"4"),(5,"5"))
#CHOICE_TIPO_CASA = ((1,"Madera rolliza"),(2,"Adobe"),(3,"Tabla"),
#                    (4,"Minifalda"),(5,"Ladrillo o Bloque"))

#class Piso(models.Model):
#    nombre = models.CharField(max_length=100)

#    def __unicode__(self):
#        return self.nombre
#        
#    class Meta:
#        verbose_name_plural = "Pisos"
        #app_label = "Indicador 15 Propiedades y Bienes"
        #db_table = "simas_piso"

#class Techo(models.Model):
#    nombre = models.CharField(max_length=100)

#    def __unicode__(self):
#        return self.nombre
#        
#    class Meta:
#        verbose_name_plural = "Techos"
        #app_label = "Indicador 15 Propiedades y Bienes"
        #db_table = "simas_techo"

#class TipoCasa(models.Model):
#    '''Modelo tipos de casa
#    '''
#    tipo = models.IntegerField('Tipo de la casa', choices=CHOICE_TIPO_CASA)
#    piso = models.ManyToManyField(Piso, verbose_name="Piso")
#    techo = models.ManyToManyField(Techo, verbose_name="Techo")
#    encuesta = models.ForeignKey(Encuesta)
#    
#    def __unicode__(self):
#        return u'%s' % self.get_tipo_display()

#    class Meta:
#        verbose_name_plural = "Tipos de Casas"
        #app_label = "Indicador 15 Propiedades y Bienes"
        #db_table = "simas_tipocasa"

#CHOICE_AMBIENTE = ((1,"1"),(2,"2"),(3,"3"),(4,"4"),(5,"5"))

#class DetalleCasa(models.Model):
#    '''Modelo detalle de casa
#    '''
#    tamano = models.IntegerField('Tamaño en mt cuadrado',null=True, blank=True)
#    ambientes = models.IntegerField(choices=CHOICE_AMBIENTE,null=True, blank=True)
#    letrina = models.IntegerField(choices=CHOICE_OPCION,null=True, blank=True)
#    lavadero = models.IntegerField(choices=CHOICE_OPCION,null=True, blank=True)
#    encuesta = models.ForeignKey(Encuesta)
#    
#    def __unicode__(self):
#        return u'%s' % str(self.tamano)

#    class Meta:
#        verbose_name_plural = "Detalle casa"
        #app_label = "Indicador 15 Propiedades y Bienes"
        #db_table = "simas_detallecasa"

#class Equipos(models.Model):
#    nombre = models.CharField(max_length=100)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Propiedades-Equipos"
        #app_label = "Indicador 15 Propiedades y Bienes"
        #db_table = "simas_equipos"


#class Infraestructuras(models.Model):
#    nombre = models.CharField(max_length=100)
#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Propiedades-Infraestructura"
        #app_label = "Indicador 15 Propiedades y Bienes"
        #db_table = "simas_infraestructuras"

#class Propiedades(models.Model):
#    '''Modelo propiedades
#    '''
#    equipo = models.ForeignKey(Equipos, null=True, blank=True)
#    cantidad_equipo = models.IntegerField(null=True, blank=True)
#    infraestructura = models.ForeignKey(Infraestructuras, null=True, blank=True)
#    cantidad_infra = models.IntegerField('Cantidad', null=True, blank=True)
#    encuesta = models.ForeignKey(Encuesta)
    
#    def __unicode__(self):
#        return u'%s' % self.equipo.nombre
#    
#    class Meta:
#        verbose_name_plural = "Propiedades"
#        #app_label = "Indicador 15 Propiedades y Bienes"
#        #db_table = "simas_propiedades"


#class NombreHerramienta(models.Model):
#    nombre = models.CharField(max_length=100)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Herramientas-Nombres"
        #app_label = "Indicador 15 Propiedades y Bienes"
        #db_table = "simas_nombreherramienta"


#class Herramientas(models.Model):
#    '''Modelo herramientas
#    '''
#    herramienta = models.ForeignKey(NombreHerramienta)
#    numero = models.IntegerField(null=True, blank=True)
#    encuesta = models.ForeignKey(Encuesta)

#    def __unicode__(self):
#        return self.herramienta.nombre

#    class Meta:
#        verbose_name_plural = "Herramientas"
        #app_label = "Indicador 15 Propiedades y Bienes"
        #db_table = "simas_herramienta"


#class NombreTransporte(models.Model):
#    nombre = models.CharField(max_length=100)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Transporte-Nombre"
        #app_label = "Indicador 15 Propiedades y Bienes"
        #db_table = "simas_nombretransporte"


#class Transporte(models.Model):
#    '''Modelo transporte
#    '''
#    transporte = models.ForeignKey(NombreTransporte)
#    numero = models.IntegerField(null=True, blank=True)
#    encuesta = models.ForeignKey(Encuesta)
#    
#    def __unicode__(self):
#        return u'%s' % self.transporte.nombre
#    
#    class Meta:
#        verbose_name_plural = "Transporte"
        #app_label = "Indicador 15 Propiedades y Bienes"
        #db_table = "simas_transporte"

#-------------------------------------------------------------------------------

## Indicador 16. Ahorro

#CHOICE_AHORRO = ((1,"Si"),(2,"No"),(3,"Menos de 5 años"),
#                 (4,"Mas de 5 años"),(5,"Hombre"),(6,"Mujer"),
#                 (7,"Ambos"))
#class AhorroPregunta(models.Model):
#    nombre = models.CharField(max_length=200)
#    class Meta:
#        verbose_name_plural = "Ahorro-Preguntas"   
#    def __unicode__(self):
#        return self.nombre
#    
#class Ahorro(models.Model):
#    ''' modelos ahorro
#    '''
#    ahorro = models.ForeignKey(AhorroPregunta)
#    respuesta = models.IntegerField(choices=CHOICE_AHORRO)
#    encuesta = models.ForeignKey(Encuesta)
#    
#    def __unicode__(self):
#        return self.ahorro.nombre
#    
#    class Meta:
#        verbose_name_plural = "Ahorro"
#        #app_label = "Indicador 16 Ahorro"
#        #db_table = "simas_ahorro"

##-------------------------------------------------------------------------------

## Indicador 17. Crédito en efectivo o materiales

#class DaCredito(models.Model):
#    nombre = models.CharField(max_length=100)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Credito-Dacredito"
#        #app_label = "Indicador 17 Credito"
#        #db_table = "simas_dacredito"


#class OcupaCredito(models.Model):
#    nombre = models.CharField(max_length=100)
#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Credito-Ocupa"
#        #app_label = "Indicador 17 Credito"
#        #db_table = "simas_ocupacredito"

#CHOICE_SATISFACCION = ((1,"Menos de 25 % de las necesidades"),
#                       (2,"Entre 25 y 50 % de las necesidades"),
#                       (3,"Entre 50 y 100 % de las necesidades"))

#class Credito(models.Model):
#    ''' Modelo de credito
#    '''
#    recibe = models.IntegerField('Recibe Crédito', choices= CHOICE_OPCION,
#                                 null=True, blank=True)
#    desde = models.IntegerField('Desde cuando', choices= CHOICE_DESDE,
#                                 null=True, blank=True)
#    quien_credito = models.ManyToManyField(DaCredito, verbose_name="De quien recibe credito",
#                                           null=True, blank=True)
#    ocupa_credito = models.ManyToManyField(OcupaCredito, verbose_name="Para que ocupa el credito",
#                                           null=True, blank=True)
#    satisfaccion = models.IntegerField('Satisfacción de la demanda de crédito',
#                                       choices= CHOICE_SATISFACCION, blank=True, null=True)
#    dia = models.IntegerField('Esta al dia con su Crédito', choices=CHOICE_OPCION,
#                              null=True, blank=True)
#    encuesta = models.ForeignKey(Encuesta)
#    
#    def __unicode__(self):
#        return u'%s' % self.get_recibe_display()
#    
#    class Meta:
#        verbose_name_plural = "Credito"
#        #app_label = "Indicador 17 Credito"
#        #db_table = "simas_credito"

##-------------------------------------------------------------------------------

## Indicador 18. Seguridad alimentaria

#class Alimentos(models.Model):
#    nombre = models.CharField(max_length=100)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Seguridad-Alimento"
#        #app_label = "Indicador 18 Seguridad Alimentaria"
#        #db_table = "simas_alimentos"

#class Seguridad(models.Model):
#    ''' Modelo Seguridad alimentaria
#    '''
#    alimento = models.ForeignKey(Alimentos)
#    producen = models.IntegerField('Producen en la finca', choices=CHOICE_OPCION)
#    compran = models.IntegerField('Compran para completar la necesidad', choices=CHOICE_OPCION)
#    consumen = models.IntegerField('Consumen lo necesario en los meses de verano', choices=CHOICE_OPCION)
#    consumen_invierno = models.IntegerField('Consumen lo necesario en los meses de invierno', choices=CHOICE_OPCION)
#    encuesta = models.ForeignKey(Encuesta)
#    
#    def __unicode__(self):
#        return u'%s' % self.alimento.nombre
#    
#    class Meta:
#        verbose_name_plural = "Seguridad"
#        #app_label = "Indicador 18 Seguridad Alimentaria"
#        #db_table = "simas_seguridad"

##-------------------------------------------------------------------------------

## Indicador 19. cuales son los riesgos que hace la finca vulnerable

#class Causa(models.Model):
#    nombre = models.CharField(max_length=100)
#    
#    def __unicode__(self):
#        return self.nombre
#        
#    class Meta:
#        verbose_name_plural = "Vulnerable - causa"
#        #app_label = "Indicador 19 Riesgo Finca vulnerable"
#        #db_table = "simas_causa"
#        
#class Fenomeno(models.Model):
#    causa = models.ForeignKey(Causa)
#    nombre = models.CharField(max_length=100)
#    
#    def __unicode__(self):
#        return '%s - %s' % (self.causa.nombre, self.nombre)
#        
#    class Meta:
#        verbose_name_plural = "Vulnerable - causa + fenomeno"
#        #app_label = "Indicador 19 Riesgo Finca vulnerable"
#        #db_table = "simas_fenomeno"
#        
#class Graves(models.Model):
#    nombre = models.CharField(max_length=100)
#    
#    def __unicode__(self):
#        return self.nombre
#        
#    class Meta:
#        verbose_name_plural = "Vulnerable - daños graves"
#        #app_label = "Indicador 19 Riesgo Finca vulnerable"
#        #db_table = "simas_graves"
#        
#class Vulnerable(models.Model):
#    ''' 20 modelo vulnerable
#    '''
#    motivo = models.ForeignKey(Fenomeno)
#    respuesta = models.ManyToManyField(Graves, verbose_name="¿Casa cuanto hay daños graves en la finca?")
#    encuesta = models.ForeignKey(Encuesta)
#    
#    class Meta:
#        verbose_name_plural = "Vulnerable"
        #app_label = "Indicador 19 Riesgo Finca vulnerable"
        #db_table = "simas_vulnerable"

#-------------------------------------------------------------------------------

# Indicador 20. Mitigación de riesgos

#class PreguntaRiesgo(models.Model):
#    nombre = models.CharField(max_length=200)

#    def __unicode__(self):
#        return self.nombre

#    class Meta:
#        verbose_name_plural = "Riesgo - pregunta"
#        #app_label = "Indicador 20 Mitigacion de riesgos"
#        #db_table = "simas_preguntariesgo"

#class Riesgos(models.Model):
#    ''' 20 mitigacion de los riesgos
#    '''
#    pregunta = models.ForeignKey(PreguntaRiesgo)
#    respuesta = models.IntegerField('Respuesta', choices=CHOICE_DESDE)
#    encuesta = models.ForeignKey(Encuesta)
#    
#    class Meta:
#        verbose_name_plural = "Riesgos"
        #app_label = "Indicador 15 Propiedades y Bienes"
        #db_table = "simas_riesgos"

#-------------------------------------------------------------------------------
