# -*- coding: UTF-8 -*-

from django.db import models
from monitoreo.lugar.models import Comunidad
from django.conf import settings

# Create your models here.
class Recolector(models.Model):
    ''' Esta es la clase para el nombre del recolector
    '''
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Recolector"

class Organizaciones(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

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
    organizacion = models.ForeignKey(Organizaciones)
    
    def __unicode__(self):
        return self.nombre

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
    automedica = models.IntegerField('Se automedica', choices=CHOICE_SALUD)
    encuesta = models.ForeignKey(Encuesta)
    
    def __unicode__(self):
        return u'%s' % self.get_sexo_display()

#-------------------------------------------------------------------------------

class PreguntaEnergia(models.Model):
    pregunta = models.CharField(max_length=200)

    def __unicode__(self):
        return self.pregunta

    class Meta:
        verbose_name_plural = "Pregunta sobre energia"

class Energia(models.Model):
    ''' 1.3 energia
    '''
    pregunta = models.ForeignKey(PreguntaEnergia)
    respuesta = models.IntegerField(choices=CHOICE_OPCION)
    encuesta = models.ForeignKey(Encuesta)

#-------------------------------------------------------------------------------

class Fuente(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Fuentes de consumo de agua"

class Tratamiento(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tratamiento de agua de consumo"

class Disponibilidad(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Disponibilidad de agua para consumo"

class Agua(models.Model):
    ''' 1.4 Agua de consumo
    '''
    fuente = models.ManyToManyField(Fuente, verbose_name="Fuente de consumo de agua")
    trata = models.ManyToManyField(Tratamiento, verbose_name="¿Cómo se trata el agua para consumo")
    disponible = models.ManyToManyField(Disponibilidad, verbose_name="Disponibilidad de agua para consumo")
    encuesta = models.ForeignKey(Encuesta)

#-------------------------------------------------------------------------------

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
        verbose_name_plural = "Porque queiere ser miembro"

CHOICE_DESDE = ((1,'Menos de 5 años'),(2,'Más de 5 años'))
CHOICE_MIEMBRO_GREMIAL = ((1,'Junta directiva'),(2,'Comisiones de trabajo'),(3,'No'))


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
    ''' 2.1 Organizacion gremial
    '''
    numero = models.IntegerField('¿Cuántas organizaciones están activas en la localidad o comunidad')
    pertence = models.IntegerField('¿Pertenece a algunas organizaciones?', choices=CHOICE_OPCION)
    cual_organizacion = models.ManyToManyField(OrgComunitarias, verbose_name="¿A cuál organización comunitaria pertenece?")
    cual_beneficio = models.ManyToManyField(BeneficioOrgComunitaria, verbose_name="¿Cuáles son los beneficios de estar organizado")
    no_organizado = models.ManyToManyField(NoOrganizado, verbose_name="¿Porqué no esta organizado?")
    encuesta = models.ForeignKey(Encuesta)

#-------------------------------------------------------------------------------

# Indicador 3 y 4. Tipo de tenencia de parcela y solar y Documento legal de la propiedad, a nombre de quién

CHOICE_TENENCIA = ((1,"Propia con escritura pública"),(2,"Propia por herencia"),
                   (3,"Propias con promesa de venta"),(4,"Propias con titulo de reforma agraria"),
                   (5,"Arrendada"),(6,"Sin documento"))
CHOICE_DUENO = ((1,"Hombre"),(2,"Mujer"),(3,"Mancomunado"),(4,"Parientes"),
                (5,"Colectivo"),(6,"No hay"))

class Tenencia(models.Model):
    ''' Modelo tipo de tenencia de la propiedad
    '''
    parcela = models.IntegerField('Parcela (tierra)', choices=CHOICE_TENENCIA)
    solar = models.IntegerField('Solar (dónde está la vivienda)', choices=CHOICE_TENENCIA)
    dueno = models.IntegerField('Documento legal de la propiedad, a nombre de quien', choices=CHOICE_DUENO)
    encuesta = models.ForeignKey(Encuesta)

#-------------------------------------------------------------------------------

# Indicador 5 Uso de Tierrra

class Uso(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Uso de tierra"

class UsoTierra(models.Model):
    ''' Uso de tierra
    '''
    tierra = models.ForeignKey(Uso, verbose_name="Uso de Tierra")
    area = models.FloatField('Área en Mz')
    encuesta = models.ForeignKey(Encuesta)

#-------------------------------------------------------------------------------

# Indicador 6. Existencia de arboles en la finca por tipo de uso

class Maderable(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Arboles maderables"

class Forrajero(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Arboles forrageros"

class Energetico(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Arboles energeticos"

class Frutal(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Arboles frutal"

class ExistenciaArboles(models.Model):
    ''' Existencia de arboles en la finca
        por tipo de uso
    '''
    maderable = models.ManyToManyField(Maderable, verbose_name="Maderable")
    cantidad_maderable = models.IntegerField()
    forrajero = models.ManyToManyField(Forrajero, verbose_name="Forrajero")
    cantidad_forrajero = models.IntegerField()
    energetico = models.ManyToManyField(Energetico, verbose_name="Energetico")
    cantidad_energetico = models.IntegerField()
    frutal = models.ManyToManyField(Frutal, verbose_name="Frutal")
    cantidad_frutal = models.IntegerField()
    encuesta = models.ForeignKey(Encuesta)

#-------------------------------------------------------------------------------

# Indicador 7. Reforestación (periodo de referencia de mayo 2009 a abril 2010)

class Actividad(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Actividades de reforestacion"

class Reforestacion(models.Model):
    ''' reforestacion
    '''
    reforestacion = models.ForeignKey(Actividad, verbose_name="Actividades de reforestación")
    cantidad = models.IntegerField('Cantidad de arboles sembrados')
    encuesta = models.ForeignKey(Encuesta)

#-------------------------------------------------------------------------------

# Indicador 8. Animales en la finca y la producción (periodo de referencia de mayo 2009 a abril 2010)

class Animales(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Finca - Animales"

class ProductoAnimal(models.Model):
    nombre = models.CharField(max_length=100)
    unidad = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Finca - Producto"


class AnimalesFinca(models.Model):
    ''' Modelo animales en la finca
    '''
    animales = models.ForeignKey(Animales)
    cantidad = models.FloatField()
    produccion = models.ForeignKey(ProductoAnimal)
    consumo = models.FloatField('Consumo')
    venta_libre = models.FloatField('Venta libre')
    venta_organizada = models.FloatField('Venta organizada')
    encuesta = models.ForeignKey(Encuesta)

#-------------------------------------------------------------------------------

# Indicador 9. Cultivos en la finca (periodo de referencia de mayo 2009 a abril 2010)

class Cultivos(models.Model):
    nombre = models.CharField(max_length=50)
    unidad = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "CultivosFinca-Cultivos"


class CultivosFinca(models.Model):
    ''' indicador cultivos en la finca
    '''
    cultivos = models.ForeignKey(Cultivos)
    area =  models.FloatField('Área/Mz')
    total = models.FloatField('Total producción por año')
    consumo = models.FloatField('Consumo por año')
    venta_libre = models.FloatField('Venta libre por año')
    venta_organizada = models.FloatField('Venta organizada por año')
    encuesta = models.ForeignKey(Encuesta)

#-------------------------------------------------------------------------------

# Indicador 10. Opciones de manejo agroecologico

class ManejoAgro(models.Model):
    nombre = models.CharField(max_length=50)
    unidad = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Uso opciones de manejo agroecologico"

CHOICE_NIVEL_CONOCIMIENTO = ((1,'Nada'),(2,'Poco'),(3,'Algo'),(4,'Bastante'))

class OpcionesManejo(models.Model):
    ''' opciones de manejo agroecologico
    '''
    uso = models.ForeignKey(ManejoAgro, verbose_name="Uso de opciones de manejo agroecologico")
    nivel = models.IntegerField('Nivel de conocimiento', choices=CHOICE_NIVEL_CONOCIMIENTO)
    menor_escala = models.IntegerField('Han experimentado en pequeña escala', choices=CHOICE_OPCION)
    mayor_escala = models.IntegerField('Han experimentado en mayor escala', choices=CHOICE_OPCION)
    volumen = models.FloatField('¿Qué área, número o volumen')
    encuesta = models.ForeignKey(Encuesta)

#-------------------------------------------------------------------------------

# Indicador 11. uso de semilla

class CultivosVariedad(models.Model):
    cultivo = models.CharField(max_length=200)

    def __unicode__(self):
        return self.cultivo

    class Meta:
        verbose_name_plural = "Cultivos variedad"

class Variedades(models.Model):
    cultivo = models.ForeignKey(CultivosVariedad)
    variedad = models.CharField(max_length=200)

    def __unicode__(self):
        return '%s - %s' % (self.cultivo.cultivo, self.variedad)

    class Meta:
        verbose_name_plural = "Variedades"

CHOICE_ORIGEN = ((1,'Nativo'), (2,'Introducido'))

class Semilla(models.Model):
    ''' uso de semilla
    '''
    cultivo = models.ForeignKey(Variedades, verbose_name="cultivo y su variedad",
                                help_text="Escoja el cultivo con su variedad")
    origen = models.IntegerField('Origen', choices=CHOICE_ORIGEN)
    encuesta = models.ForeignKey(Encuesta)

#-------------------------------------------------------------------------------

# Indicador 12. Suelo

class Textura(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Suelo - Textura"

class Profundidad(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Suelo - Profundidad"

# Esta clase de va a ocupar en varias de los tipos de caraterización
# ya que contendra las opciones Alta, Media y Baja
class Densidad(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Suelo - Densidad"

class Pendiente(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Suelo - Pendiente"

class Drenaje(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Suelo Drenaje"

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

# 12.2 Manejo de suelo

class Preparar(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "ManejoSuelo - preparar"

class Traccion(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "ManejoSuelo - tracción"

class Fertilizacion(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "ManejoSuelo - fertilizacion"

class Conservacion(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "ManejoSuelo - conservacion"

class ManejoSuelo(models.Model):
    ''' 12.2 Manejo de suelo
    '''
    preparan = models.ManyToManyField(Preparar, verbose_name="¿Cómo preparan sus terrenos?")
    traccion = models.ManyToManyField(Traccion,
                                      verbose_name="¿Qué tipo de traccion utiliza para la preparación del suelo?")
    analisis = models.IntegerField('¿Realiza análisis de fertilidad del suelo', choices=CHOICE_OPCION)
    fertilizacion = models.ManyToManyField(Fertilizacion, verbose_name="¿Qué tipo de fertilización realiza")
    practica = models.IntegerField('¿Realiza práctica de conservación de suelo', choices=CHOICE_OPCION)
    obra = models.ManyToManyField(Conservacion, verbose_name="¿Qué tipo de obra de conservación de suelo?")
    encuesta = models.ForeignKey(Encuesta)

#-------------------------------------------------------------------------------

# Indicador 13 -  Ingreso Familiar. Venta de rubros (periodo de referencia de mayo 2009 a abril 2010)

CHOICE_VENDIO = ((1,"Comunidad"),(2,"Intermediario"),(3,"Mercado"),
                 (4,"Cooperativa"),(5,'todos'))

CHOICE_MANEJA = ((1,"Hombre"),(2,"Mujer"),(3,"Ambos"),(4,"Hijos/as"),
                 (5,'Hombre-Hijos'),(6,'Mujer-Hijos'),(7,'Todos'))

class Rubros(models.Model):
    nombre = models.CharField(max_length=50)
    unidad = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "IngresoFamiliar-Rubros"
    def __unicode__(self):
        return self.nombre

class IngresoFamiliar(models.Model):
    ''' Modelo Ingreso familiar. venta de rubros
    '''
    rubro = models.ForeignKey(Rubros)
    cantidad = models.IntegerField('Cantidad vendida en el año pasado',null=True, blank=True)
    precio = models.IntegerField('Precio de venta por unidad',null=True, blank=True)
    quien_vendio = models.IntegerField('¿A quien vendio?', choices=CHOICE_VENDIO,null=True, blank=True)
    maneja_negocio = models.IntegerField('¿Quién maneja el negocio', choices=CHOICE_MANEJA,null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)

#-------------------------------------------------------------------------------

# Indicador 14 Otros ingresos.

class Fuentes(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Otros-Ingreso - Fuentes"

class TipoTrabajo(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Otro-Ingreso - TipoTrabajo"

class OtrosIngresos(models.Model):
    '''Otros ingresos
    '''
    fuente = models.ForeignKey(Fuentes)
    tipo = models.ForeignKey(TipoTrabajo)
    meses = models.IntegerField('# Meses',null=True, blank=True)
    ingreso = models.IntegerField('Ingreso por mes',null=True, blank=True)
    tiene_ingreso = models.IntegerField(choices=CHOICE_MANEJA,null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)

#-------------------------------------------------------------------------------

# Indicador 15. Propiedades y Bienes

CHOICE_AMBIENTE = ((1,"1"),(2,"2"),(3,"3"),(4,"4"),(5,"5"))
CHOICE_TIPO_CASA = ((1,"Madera rolliza"),(2,"Adobe"),(3,"Tabla"),
                    (4,"Minifalda"),(5,"Ladrillo o Bloque"))

class Piso(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

class Techo(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

class TipoCasa(models.Model):
    '''Modelo tipos de casa
    '''
    tipo = models.IntegerField('Tipo de la casa', choices=CHOICE_TIPO_CASA)
    piso = models.ManyToManyField(Piso, verbose_name="Piso")
    techo = models.ManyToManyField(Techo, verbose_name="Techo")
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "Tipos de Casas"

CHOICE_AMBIENTE = ((1,"1"),(2,"2"),(3,"3"),(4,"4"),(5,"5"))

class DetalleCasa(models.Model):
    '''Modelo detalle de casa
    '''
    tamano = models.IntegerField('Tamaño en mt cuadrado',null=True, blank=True)
    ambientes = models.IntegerField(choices=CHOICE_AMBIENTE,null=True, blank=True)
    letrina = models.IntegerField(choices=CHOICE_OPCION,null=True, blank=True)
    lavadero = models.IntegerField(choices=CHOICE_OPCION,null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "Detalles de la Casa"

class Equipos(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Propiedades-Equipos"


class Infraestructuras(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Propiedades-Infraestructura"


CHOICE_EQUIPO = ((1,"Tiene Luz"),(2,"Con medidor UF"),(3,"Con planta"),
                 (4,"Con panel solar o aeromotor"),(5,"Ilegal"))

class Propiedades(models.Model):
    '''Modelo propiedades
    '''
    equipo = models.ForeignKey(Equipos, null=True, blank=True)
    cantidad_equipo = models.IntegerField(null=True, blank=True)
    infraestructura = models.ForeignKey(Infraestructuras, null=True, blank=True)
    cantidad_infra = models.IntegerField('Cantidad', null=True, blank=True)
    tipo_equipo = models.IntegerField(choices=CHOICE_EQUIPO, null=True, blank=True)
    respuesta = models.IntegerField(choices=CHOICE_OPCION, null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)


class NombreHerramienta(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Herramientas-Nombres"


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


class NombreTransporte(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Transporte-Nombre"


class Transporte(models.Model):
    '''Modelo transporte
    '''
    transporte = models.ForeignKey(NombreTransporte)
    numero = models.IntegerField(null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)

#-------------------------------------------------------------------------------

# Indicador 16. Ahorro

CHOICE_AHORRA_QUIEN = ((1,'Hombre'),(2,'Mujer'),(3,'Hijos'),(4,'Hombre-Mujer'))

class Ahorro(models.Model):
    ''' modelo ahorro
    '''
    tiene_ahorro = models.IntegerField('tiene ahorro en efectivo', choices=CHOICE_OPCION)
    tiene_joya = models.IntegerField('tiene ahorro en joyeria/prenda', choices=CHOICE_OPCION)
    desde_ahorra = models.IntegerField('Desde cuando ahorra', choices=CHOICE_DESDE)
    posee_ahorro = models.IntegerField('Posee una cuenta de ahorro', choices=CHOICE_OPCION)
    quien_ahorro = models.IntegerField('Ahorra a nombre de quien', choices=CHOICE_AHORRA_QUIEN)
    interesado_ahorro = models.IntegerField('¿Si no tiene ahorro, está interesado en ahorrar en una cuenta de ahorro?', CHOICE_OPCION)
    encuesta = models.ForeignKey(Encuesta)

#-------------------------------------------------------------------------------

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
                       (3,"Entre 50 y 100 % de las necesidades"))

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

#-------------------------------------------------------------------------------

# Indicador 18. Seguridad alimentaria

class Alimentos(models.Model):
    nombre = models.CharField(max_length=100)

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

#-------------------------------------------------------------------------------

# Indicador 19. cuales son los riesgos que hace la finca vulnerable
class Causa(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Vulnerable - causa"
        
class Fenomeno(models.Model):
    causa = models.ForeignKey(Causa)
    nombre = models.CharField(max_length=100)
    
    def __unicode__(self):
        return '%s - %s' % (self.causa.nombre, self.nombre)
        
    class Meta:
        verbose_name_plural = "Vulnerable - causa + fenomeno"
        
class Graves(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Vulnerable - daños graves"
        
class Vulnerable(models.Model):
    ''' 20 modelo vulnerable
    '''
    motivo = models.ForeignKey(Fenomeno)
    respuesta = models.ManyToManyField(Graves, verbose_name="¿Casa cuanto hay daños graves en la finca?")
    encuesta = models.ForeignKey(Encuesta)

#-------------------------------------------------------------------------------

# Indicador 20. Mitigación de riesgos

class PreguntaRiesgo(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Riesgo - pregunta"

class Riegos(models.Model):
    ''' 20 mitigacion de los riesgos
    '''
    pregunta = models.ForeignKey(PreguntaRiesgo)
    respuesta = models.IntegerField('Respuesta', choices=CHOICE_DESDE)
    encuesta = models.ForeignKey(Encuesta)

#-------------------------------------------------------------------------------
