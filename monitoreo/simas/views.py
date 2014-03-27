 # -*- coding: utf-8 -*-
from django.http import Http404, HttpResponse
from django.template.defaultfilters import slugify
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.generic.simple import direct_to_template
from django.utils import simplejson
from django.db.models import Sum, Count, Avg
from django.core.exceptions import ViewDoesNotExist
import random

from monitoreo.simas.models import *
from monitoreo.indicador01.models import *
from monitoreo.indicador02.models import *
from monitoreo.indicador05.models import *
from monitoreo.indicador06.models import *
from monitoreo.indicador07.models import *
from monitoreo.indicador08.models import *
from monitoreo.indicador09.models import *
from monitoreo.indicador10.models import *
from monitoreo.indicador11.models import *
from monitoreo.indicador12.models import *
from monitoreo.indicador13.models import *
from monitoreo.indicador14.models import *
from monitoreo.indicador15.models import *
from monitoreo.indicador16.models import *
from monitoreo.indicador17.models import *
from monitoreo.indicador18.models import *
from monitoreo.indicador19.models import *
from monitoreo.indicador20.models import *

from decorators import session_required
from datetime import date
import datetime
from monitoreo.simas.forms import *
from monitoreo.lugar.models import *
from decimal import Decimal
from utils import grafos
from utils import *

# Create your views here.

# Función para obtener las url

def _get_view(request, vista):
    if vista in VALID_VIEWS:
        return VALID_VIEWS[vista](request)
    else:
        raise ViewDoesNotExist("Tried %s in module %s Error: View not defined in VALID_VIEWS." % (vista, 'simas.views'))

#-------------------------------------------------------------------------------

def _queryset_filtrado(request):
    '''metodo para obtener el queryset de encuesta
    segun los filtros del formulario que son pasados
    por la variable de sesion'''
    #anio = int(request.session['fecha'])
    #diccionario de parametros del queryset
    params = {}
    if 'fecha' in request.session:
        params['year__in'] = request.session['fecha']

    if request.session['departamento']:
        if not request.session['municipio']:
            municipios = Municipio.objects.filter(departamento__in=request.session['departamento'])
            params['comunidad__municipio__in'] = municipios
        else:
            if request.session['comunidad']:
                params['comunidad__in'] = request.session['comunidad']
            else:
                params['comunidad__municipio__in'] = request.session['municipio']

    if request.session['organizacion']:
        params['organizacion__in'] = request.session['organizacion']

#        if 'departamento' in request.session:
#            #incluye municipio y comunidad
#            if request.session['municipio']:
#                if 'comunidad' in request.session:
#                    params['comunidad'] = request.session['comunidad']
#                else:
#                    params['comunidad__municipio'] = request.session['municipio']
#            else:
#                params['comunidad__municipio__departamento'] = request.session['departamento']

#        if 'organizacion' in request.session:
#            params['organizacion'] = request.session['organizacion']

    if 'socio' in request.session:
        params['organizaciongremial__socio'] = request.session['socio']

    if 'desde' in request.session:
        params['organizaciongremial__desde_socio'] = request.session['desde']

    if 'duenio' in  request.session:
        params['tenencia__dueno'] = request.session['duenio']

    unvalid_keys = []
    for key in params:
        if not params[key]:
            unvalid_keys.append(key)

    for key in unvalid_keys:
        del params[key]

    return Encuesta.objects.filter(**params)

#-------------------------------------------------------------------------------

# Comienza la parte del index

def inicio(request):
    #centinela = 0
    if request.method == 'POST':
        mensaje = None
        form = MonitoreoForm(request.POST)
        if form.is_valid():
            request.session['fecha'] = form.cleaned_data['fecha']
            request.session['departamento'] = form.cleaned_data['departamento']
            request.session['organizacion'] = form.cleaned_data['organizacion']
            request.session['municipio'] = form.cleaned_data['municipio']
            request.session['comunidad'] = form.cleaned_data['comunidad']
            request.session['socio'] = form.cleaned_data['socio']
            request.session['desde'] = form.cleaned_data['desde']
            request.session['duenio'] = form.cleaned_data['dueno']

            mensaje = "Todas las variables estan correctamente :)"
            request.session['activo'] = True
            centinela = 1
            variablerandom = random.randrange(10,250)
            request.session['crce']  = variablerandom
        else:
            centinela = 0   
           
    else:
        form = MonitoreoForm()
        mensaje = "Existen alguno errores"
        centinela = 0
        if 'fecha' in request.session:
            del request.session['fecha']
            del request.session['departamento']
            del request.session['organizacion']
            del request.session['municipio']
            del request.session['comunidad']
            del request.session['socio']
            del request.session['desde']
            del request.session['duenio']

    #dict = {'form': form,'user': request.user,'centinela':centinela}
    return render_to_response('simas/inicio.html', locals(),
                              context_instance=RequestContext(request))

#-------------------------------------------------------------------------------

def index(request):
    familias = Encuesta.objects.all().count()
    organizacion = Organizaciones.objects.all().count()
    mujeres = Encuesta.objects.filter(sexo=2).count()
    hombres = Encuesta.objects.filter(sexo=1).count()

    return direct_to_template(request, 'index.html', locals())

#-------------------------------------------------------------------------------
# para presentar listado de zonas

#def listado_zonas(request,zona):
#    organizaciones = Organizaciones.objects.filter(organizacion__zona=zona)

#-------------------------------------------------------------------------------

def generales(request):
    total_encuesta = Encuesta.objects.all().count()

    mujeres = Encuesta.objects.filter(sexo=2).count()
    por_mujeres = round(saca_porcentajes(mujeres,total_encuesta),2)
    hombres = Encuesta.objects.filter(sexo=1).count()
    por_hombres = round(saca_porcentajes(hombres,total_encuesta),2)

    #Educacion
    escolaridad = []
    valores_e = []
    leyenda_e = []
    for escuela in CHOICE_EDUCACION:
        conteo = Encuesta.objects.filter(educacion__sexo=escuela[0]).aggregate(conteo=Count('educacion__sexo'))['conteo']
        porcentaje = round(saca_porcentajes(conteo,total_encuesta),2)
        escolaridad.append([escuela[1],conteo,porcentaje])
        valores_e.append(conteo)
        leyenda_e.append(escuela[1])

    #Departamentos
    depart = []
    valores_d = []
    leyenda_d = []
    for depar in Departamento.objects.all():
        conteo = Encuesta.objects.filter(comunidad__municipio__departamento=depar).aggregate(conteo=Count('comunidad__municipio__departamento'))['conteo']
        porcentaje = round(saca_porcentajes(conteo,total_encuesta))
        if conteo != 0:
            depart.append([depar.nombre,conteo,porcentaje])
            valores_d.append(conteo)
            leyenda_d.append(depar.nombre)

    #Municipios
    munis = []
    valores_m = []
    leyenda_m = []
    for mun in Municipio.objects.all():
        conteo = Encuesta.objects.filter(comunidad__municipio=mun).aggregate(conteo=Count('comunidad__municipio'))['conteo']
        porcentaje = round(saca_porcentajes(conteo,total_encuesta))
        if conteo != 0:
            munis.append([mun.nombre,conteo,porcentaje])
            valores_m.append(conteo)
            leyenda_m.append(mun.nombre)

    #encuestas por año
    ANOS_CHOICES_P = [(numero, numero) for numero in range(datetime.date.today().year, 2000, -1)]
    anio_lista = []
    for anio in ANOS_CHOICES_P:
        conteo = Encuesta.objects.filter(fecha__year=anio[0]).count()
        if conteo > 0:
            porcentaje = round(saca_porcentajes(conteo,total_encuesta),1)
            anio_lista.append([anio[1],conteo,porcentaje])

    #Lista de las encuestas por organizacion
    lista_encuesta = {}
    for lista in Organizaciones.objects.all():
        todo = Encuesta.objects.filter(organizacion=lista)

        lista_encuesta[lista] = todo

    #lista de recolectores con sus encuestas
    lista_recolectores = {}
    for lista in Recolector.objects.all():
        nose = Encuesta.objects.filter(recolector=lista)
        lista_recolectores[lista] = nose

    return render_to_response('simas/generales.html', locals(),
                               context_instance=RequestContext(request))

#Comienzan las salidas del monitoreo simas

#Tabla Educación
@session_required
def educacion(request):
    '''Tabla de educacion
    '''
    #*******Variables globales**********
    a = _queryset_filtrado(request)
    num_familias = a.count()
    #**********************************

    tabla_educacion = []
    grafo = []
    suma = 0
    for e in CHOICE_EDUCACION:
        objeto = a.filter(educacion__sexo = e[0]).aggregate(num_total = Sum('educacion__total'),
                no_leer = Sum('educacion__no_leer'),
                p_incompleta = Sum('educacion__p_incompleta'),
                p_completa = Sum('educacion__p_completa'),
                s_incompleta = Sum('educacion__s_incompleta'),
                bachiller = Sum('educacion__bachiller'),
                universitario = Sum('educacion__universitario'),
                f_comunidad = Sum('educacion__f_comunidad'))
        try:
            suma = int(objeto['p_completa'] or 0) + int(objeto['s_incompleta'] or 0) + int(objeto['bachiller'] or 0) + int(objeto['universitario'] or 0)
        except:
            pass
        variable = round(saca_porcentajes(suma,objeto['num_total']))
        grafo.append([e[1],variable])
        fila = [e[1], objeto['num_total'],
                saca_porcentajes(objeto['no_leer'], objeto['num_total'], False),
                saca_porcentajes(objeto['p_incompleta'], objeto['num_total'], False),
                saca_porcentajes(objeto['p_completa'], objeto['num_total'], False),
                saca_porcentajes(objeto['s_incompleta'], objeto['num_total'], False),
                saca_porcentajes(objeto['bachiller'], objeto['num_total'], False),
                saca_porcentajes(objeto['universitario'], objeto['num_total'], False),
                saca_porcentajes(objeto['f_comunidad'], objeto['num_total'], False)]
        tabla_educacion.append(fila)

    return render_to_response('simas/educacion.html', locals(),
                                  context_instance=RequestContext(request))

#Tabla Salud
@session_required
def salud(request):
    '''salud'''
    #*******Variables globales**********
    a = _queryset_filtrado(request)
    num_familias = a.count()
    #**********************************

    numero = a.count()
    tabla_estado = []
    tabla_sitio = []

    for choice in CHOICE_EDUCACION:
        query = a.filter(salud__sexo=choice[0])
        casos = query.count()
        resultados = query.aggregate(bs = Sum('salud__b_salud'),
                                     ds = Sum('salud__s_delicada'),
                                     ec = Sum('salud__e_cronica'),
                                     centro = Sum('salud__v_centro'),
                                     medico = Sum('salud__v_medico'),
                                     naturista = Sum('salud__v_naturista'),
                                     automedica = Sum('salud__automedica')
                                     )

        #validando que no sea none
        if resultados['bs']:
            total_estado = resultados['bs']
        else:
            total_estado = 0

        if resultados['ds']:
            total_estado += resultados['ds']

        if resultados['ec']:
            total_estado += resultados['ec']

        fila_estado = [choice[1], casos,
                saca_porcentajes(resultados['bs'], total_estado, False),
                saca_porcentajes(resultados['ds'], total_estado, False),
                saca_porcentajes(resultados['ec'], total_estado, False)]
        tabla_estado.append(fila_estado)

        total_sitio = 0
        if resultados['centro']:
            total_sitio += resultados['centro']
        if resultados['medico']:
            total_sitio += resultados['medico']
        if resultados['naturista']:
            total_sitio += resultados['naturista']
        if resultados['automedica']:
            total_sitio += resultados['automedica']

        fila_sitio = [choice[1], casos,
                      saca_porcentajes(resultados['centro'], total_sitio, False),
                      saca_porcentajes(resultados['medico'], total_sitio, False),
                      saca_porcentajes(resultados['naturista'], total_sitio, False),
                      saca_porcentajes(resultados['automedica'], total_sitio, False),
                    ]
        tabla_sitio.append(fila_sitio)

    return render_to_response('simas/salud.html',
                              {'tabla_estado':tabla_estado,
                               'tabla_sitio': tabla_sitio,
                               'num_familias': num_familias},
                              context_instance=RequestContext(request))

#Tabla Energia
@session_required
def luz(request):
    '''Tabla de acceso a energia electrica'''
    consulta = _queryset_filtrado(request)
    tabla = []
    total_tiene_luz = 0

    for choice in PreguntaEnergia.objects.all():
        query = consulta.filter(energia__pregunta=choice, energia__respuesta=1).distinct()
        resultados = query.count()
        if choice.pregunta == 1:
            total_tiene_luz = resultados
            fila = [choice.pregunta,
                    resultados,
                    saca_porcentajes(resultados, consulta.count(), False)]
            tabla.append(fila)
        else:
            fila = [choice.pregunta,
                    resultados,
                    saca_porcentajes(resultados, consulta.count(), False)]
            tabla.append(fila)

    return render_to_response('simas/luz.html',
                              {'tabla':tabla, 'num_familias': consulta.count()},
                              context_instance=RequestContext(request))

#Tabla Agua
@session_required
def agua(request):
    '''Agua'''
    consulta = _queryset_filtrado(request)
    tabla = []
    total = consulta.aggregate(total=Count('agua__fuente'))

    for choice in Fuente.objects.all():
        query = consulta.filter(agua__fuente=choice)
        numero = query.count()
        fila = [choice.nombre, numero,
                #saca_porcentajes(numero, total['total'], False),
                saca_porcentajes(numero, consulta.count(), False)
                ]
        tabla.append(fila)

    #totales = [total['total'], 100, total['cantidad'], 100]
    totales = [consulta.count(), 100]
    return render_to_response('simas/agua.html',
                              #{'tabla':tabla, 'totales':totales},
                              {'tabla':tabla, 'num_familias': consulta.count()},
                              context_instance=RequestContext(request))

#Tabla UsoTierra
@session_required
def fincas(request):
    '''Tabla de fincas'''

    tabla = {}
    totales = {}
    consulta = _queryset_filtrado(request)
    num_familias = consulta.count()

    suma = 0
    total_manzana = 0
    por_num = 0
    por_man = 0

    for total in Uso.objects.exclude(id=1):
        conteo = consulta.filter(usotierra__tierra = total)
        suma += conteo.count()
        man = conteo.aggregate(area = Sum('usotierra__area'))['area']
        try:
            total_manzana += man
        except:
            pass

    totales['numero'] = suma
    totales['manzanas'] = round(total_manzana,0)
    totales['promedio_manzana'] = round(totales['manzanas'] / consulta.count(),2)

#    totales['numero'] = consulta.count()
#    totales['porcentaje_num'] = 100
#    totales['manzanas'] = consulta.aggregate(area=Sum('usotierra__area'))['area']
#    totales['porcentaje_mz'] = 100

#    for uso in Uso.objects.all().exclude(id=1):
#        key = slugify(uso.nombre).replace('-', '_')
#        query = consulta.filter(usotierra__tierra = uso)
#        numero = query.count()
#        porcentaje_num = saca_porcentajes(numero, totales['numero'])
#        manzanas = query.aggregate(area = Sum('usotierra__area'))['area']
#        porcentaje_mz = saca_porcentajes(manzanas, totales['manzanas'])
#        tabla[key] = {'numero': numero, 'porcentaje_num': porcentaje_num,
#                      'manzanas': manzanas, 'porcentaje_mz': porcentaje_mz}
    for uso in Uso.objects.exclude(id=1):
        key = slugify(uso.nombre).replace('-', '_')
        query = consulta.filter(usotierra__tierra = uso)
        numero = query.count()
        porcentaje_num = saca_porcentajes(numero, num_familias)
        por_num += porcentaje_num
        try:
            manzanas = query.aggregate(area = Sum('usotierra__area'))['area']
        except:
            manzanas = 0
        porcentaje_mz = saca_porcentajes(manzanas, totales['manzanas'])
        por_man += porcentaje_mz

        tabla[key] = {'numero': int(numero), 
                      'porcentaje_num': int(porcentaje_num),
                      'manzanas': manzanas, 
                      'porcentaje_mz': int(porcentaje_mz)}

    totales['porcentaje_numero'] = por_num
    totales['porcentaje_manzana'] = round(por_man,2)
    #calculando los promedios
    lista = []
    cero = 0
    rango1 = 0
    rango2 = 0
    rango3 = 0
    rango4 = 0
    for x in consulta:
        query = UsoTierra.objects.filter(encuesta=x, tierra=1).aggregate(AreaSuma=Sum('area'))
        lista.append([x.id,query])

    for nose in lista:
        if nose[1]['AreaSuma'] == 0:
            cero += 1
        if nose[1]['AreaSuma'] >= 0.1 and  nose[1]['AreaSuma'] <= 10:
            rango1 += 1
        if nose[1]['AreaSuma'] >= 11 and nose[1]['AreaSuma'] <= 25:
            rango2 += 1
        if nose[1]['AreaSuma'] >= 26 and nose[1]['AreaSuma'] <= 50:
            rango3 += 1
        if nose[1]['AreaSuma'] >=51:
            rango4 += 1
    total_rangos = cero + rango1 + rango2 + rango3 + rango4
    por_cero = round(saca_porcentajes(cero,total_rangos),2)
    por_rango1 = round(saca_porcentajes(rango1,total_rangos),2)
    por_rango2 = round(saca_porcentajes(rango2,total_rangos),2)
    por_rango3 = round(saca_porcentajes(rango3,total_rangos),2)
    por_rango4 = round(saca_porcentajes(rango4,total_rangos),2)
    total_porcentajes = round((por_cero + por_rango1 + por_rango2 + por_rango3 + por_rango4),1)


    return render_to_response('simas/fincas.html',
                              locals(),
                              context_instance=RequestContext(request))

#Tabla Existencia Arboles
@session_required
def arboles(request):
    '''Tabla de arboles'''
    #******Variables***************
    a = _queryset_filtrado(request)
    num_familias = a.count()
    #******************************

    #********Existencia de arboles sumatorias*****************
    maderable = a.aggregate(Sum('existenciaarboles__cantidad_maderable'))['existenciaarboles__cantidad_maderable__sum']
    forrajero = a.aggregate(Sum('existenciaarboles__cantidad_forrajero'))['existenciaarboles__cantidad_forrajero__sum']
    energetico = a.aggregate(Sum('existenciaarboles__cantidad_energetico'))['existenciaarboles__cantidad_energetico__sum']
    frutal = a.aggregate(Sum('existenciaarboles__cantidad_frutal'))['existenciaarboles__cantidad_frutal__sum']
    #*********************************************

    #*******promedios de arboles por familia*********
    pro_maderable = maderable / num_familias if maderable != None else 0
    pro_forrajero = forrajero / num_familias if forrajero != None else 0
    pro_energetico = energetico / num_familias if energetico != None else 0
    pro_frutal = frutal / num_familias if frutal != None else 0
    #***********************************************

    #******conteo de arboles********************
    maderablect = a.aggregate(Count('existenciaarboles__cantidad_maderable'))['existenciaarboles__cantidad_maderable__count']
    forrajeroct = a.aggregate(Count('existenciaarboles__cantidad_forrajero'))['existenciaarboles__cantidad_forrajero__count']
    energeticoct = a.aggregate(Count('existenciaarboles__cantidad_energetico'))['existenciaarboles__cantidad_energetico__count']
    frutalct = a.aggregate(Count('existenciaarboles__cantidad_frutal'))['existenciaarboles__cantidad_frutal__count']

    #**********Reforestacion************************
    tabla = {}
    totales = {}
    totales['numero'] = a.aggregate(numero = Count('reforestacion__reforestacion'))['numero']
    totales['porcentaje_nativos'] = 100
    totales['nativos'] = a.aggregate(nativo=Sum('reforestacion__cantidad'))['nativo']


    for activ in Actividad.objects.all():
        key = slugify(activ.nombre).replace('-', '_')
        query = a.filter(reforestacion__reforestacion = activ)
        numero = query.count()
        porcentaje_num = saca_porcentajes(numero, num_familias)
        nativos = query.aggregate( cantidad = Sum('reforestacion__cantidad'))['cantidad']
        totalnn = nativos
        porcentaje_nativos = saca_porcentajes(nativos, totalnn)

        tabla[key] = {'numero': numero, 'porcentaje_num':porcentaje_num,
                      'porcentaje_nativos': porcentaje_nativos,'nativos': nativos
                      }


    return  render_to_response('simas/arboles.html',
                              {'num_familias':num_familias,'maderable':maderable,
                               'forrajero':forrajero,'energetico':energetico,'frutal':frutal,
                               'pro_maderable':pro_maderable,'pro_forrajero':pro_forrajero,
                               'pro_energetico':pro_energetico,'pro_frutal':pro_frutal,
                               'maderablect':maderablect,'forrajeroct':forrajeroct,
                               'energeticoct':energeticoct,'frutalct':frutalct,
                               'tabla':tabla,'totales':totales},
                                context_instance=RequestContext(request))

#Tabla Animales en la finca
@session_required
def animales(request):
    '''Los animales y la produccion'''
    consulta = _queryset_filtrado(request)
    tabla = []
    tabla_produccion = []
    totales = {}

    totales['numero'] = consulta.count()
    totales['porcentaje_num'] = 100
    totales['animales'] = consulta.aggregate(cantidad=Sum('animalesfinca__cantidad'))['cantidad']
    totales['porcentaje_animal'] = 100

    for animal in Animales.objects.all():
        query = consulta.filter(animalesfinca__animales = animal)
        numero = query.distinct().count()
        try:
            producto = AnimalesFinca.objects.filter(animales = animal)[0].produccion
        except:
            #el animal no tiene producto aún
            continue

        porcentaje_num = saca_porcentajes(numero, totales['numero'], False)
        animales = query.aggregate(cantidad = Sum('animalesfinca__cantidad'),
                                   venta_libre = Sum('animalesfinca__venta_libre'),
                                   venta_organizada = Sum('animalesfinca__venta_organizada'),
                                   total_produccion = Sum('animalesfinca__total_produccion'),
                                   consumo = Sum('animalesfinca__consumo'))
        try:
            animal_familia = float(animales['cantidad'])/float(numero)
        except:
            animal_familia = 0
        animal_familia = "%.2f" % animal_familia
        tabla.append([animal.nombre, numero, porcentaje_num,
                      animales['cantidad'], animal_familia])
        tabla_produccion.append([animal.nombre, animales['cantidad'],
                                 producto.nombre, producto.unidad,
                                 animales['total_produccion'],
                                 animales['consumo'],
                                 animales['venta_libre'],
                                 animales['venta_organizada']])

    return render_to_response('simas/animales.html',
                              {'tabla':tabla, 'totales': totales,
                               'num_familias': consulta.count(),
                               'tabla_produccion': tabla_produccion},
                              context_instance=RequestContext(request))


#Tabla Organizacion Gremial
@session_required
def gremial(request):
    '''tabla de organizacion gremial'''
     #***********Variables***************
    a = _queryset_filtrado(request)
    num_familias = a.count()
    #***********************************

    tabla_gremial = {}
    divisor = a.aggregate(divisor=Count('organizaciongremial__socio'))['divisor']

    for i in OrgGremiales.objects.all():
        key = slugify(i.nombre).replace('-', '_')
        query = a.filter(organizaciongremial__socio = i)
        frecuencia = query.aggregate(frecuencia=Count('organizaciongremial__socio'))['frecuencia']
        porcentaje = saca_porcentajes(frecuencia,divisor)
        tabla_gremial[key] = {'frecuencia':frecuencia, 'porcentaje':porcentaje}

    #desde gremial
    tabla_desde = {}
    divisor1 = a.aggregate(divisor1=Count('organizaciongremial__desde_socio'))['divisor1']
    for k in CHOICE_DESDE:
        key = slugify(k[1]).replace('-','_')
        query = a.filter(organizaciongremial__desde_socio = k[0])
        frecuencia = query.aggregate(frecuencia=Count('organizaciongremial__desde_socio'))['frecuencia']
        porcentaje = saca_porcentajes(frecuencia,divisor1)
        tabla_desde[key] = {'frecuencia':frecuencia, 'porcentaje':porcentaje}

    #miembro
    tabla_miembro = {}
    divisor2  = a.filter(organizaciongremial__miembro_gremial__in=(1,2,3)).count()

    for p in CHOICE_MIEMBRO_GREMIAL:
        key = slugify(p[1]).replace('-','_')
        query = a.filter(organizaciongremial__miembro_gremial = p[0])
        frecuencia = query.aggregate(frecuencia=Count('organizaciongremial__miembro_gremial'))['frecuencia']
        porcentaje = saca_porcentajes(frecuencia,divisor2)
        tabla_miembro[key] = {'frecuencia':frecuencia, 'porcentaje':porcentaje}

    #desde miembro
    tabla_desde_miembro = {}
    divisor3 = a.aggregate(divisor3=Count('organizaciongremial__desde_miembro'))['divisor3']
    for k in CHOICE_DESDE:
        key = slugify(k[1]).replace('-','_')
        query = a.filter(organizaciongremial__desde_miembro = k[0])
        frecuencia = query.aggregate(frecuencia=Count('organizaciongremial__desde_miembro'))['frecuencia']
        porcentaje = saca_porcentajes(frecuencia,divisor3)
        tabla_desde_miembro[key] = {'frecuencia':frecuencia, 'porcentaje':porcentaje}

    #capacitación
    tabla_capacitacion = {}
    divisor4 = a.filter(organizaciongremial__capacitacion__in=[1,2]).count()
    for t in CHOICE_OPCION:
        key = slugify(t[1]).replace('-','_')
        query = a.filter(organizaciongremial__capacitacion = t[0])
        frecuencia = query.aggregate(frecuencia=Count('organizaciongremial__capacitacion'))['frecuencia']
        porcentaje = saca_porcentajes(frecuencia,divisor4)
        tabla_capacitacion[key] = {'frecuencia':frecuencia, 'porcentaje':porcentaje}


    return render_to_response('simas/gremial.html',
                                 {'tabla_gremial': tabla_gremial, 'tabla_desde':tabla_desde,
                                 'num_familias': num_familias,'divisor':divisor,'divisor1':divisor1,
                                 'tabla_miembro':tabla_miembro, 'divisor2':divisor2,
                                 'tabla_desde_miembro':tabla_desde_miembro, 'divisor3':divisor3,
                                 'tabla_capacitacion':tabla_capacitacion, 'divisor4':divisor4},
                                 context_instance=RequestContext(request))

#Tabla Organizacion comunitaria
@session_required
def comunitario(request):
    ''' tablas organización comunitaria '''
    #***********Variables***************
    a = _queryset_filtrado(request)
    num_familias = a.count()
    #***********************************

    #rangos
    uno = a.filter(organizacioncomunitaria__numero__range=(1,5)).count()
    dos = a.filter(organizacioncomunitaria__numero__range=(6,10)).count()
    tres = a.filter(organizacioncomunitaria__numero__gt=11).count()

    tabla_pertenece = {}
    divisor = a.filter(organizacioncomunitaria__pertence__in=[1,2]).count()
    for t in CHOICE_OPCION:
        key = slugify(t[1]).replace('-','_')
        query = a.filter(organizacioncomunitaria__pertence = t[0])
        frecuencia = query.aggregate(frecuencia=Count('organizacioncomunitaria__pertence'))['frecuencia']
        porcentaje = saca_porcentajes(frecuencia,divisor)
        tabla_pertenece[key] = {'frecuencia':frecuencia, 'porcentaje':porcentaje}



    return render_to_response('simas/comunitario.html', {'tabla_pertenece':tabla_pertenece,
                              'divisor':divisor, 'num_familias': num_familias,
                              'uno':uno,'dos':dos,'tres':tres},
                                context_instance=RequestContext(request) )

#Tabla Cultivos
def grafo_generic(request, producto):
    #******Variables***************
    a = _queryset_filtrado(request)
    grafo = {}
    tabla = {}
    for i in Cultivos.objects.filter(id=producto):
        key = slugify(i.nombre).replace('-', '_')
        query = a.filter(cultivosfinca__cultivos = i)
        for obj in query:
            cultivos_finca = obj.cultivosfinca_set.filter(cultivos__id=producto)
            for datos in cultivos_finca:
                if not key in grafo.keys():
                    grafo[key] = [[datos.area,datos.total], ]
                    tabla[key] = [[datos.area,datos.total,datos.encuesta_id], ]
                else:
                    grafo[key].append([datos.area,datos.total])
                    tabla[key].append([datos.area,datos.total,datos.encuesta_id])
    dict = {'grafo':grafo,'tabla':tabla}
    return dict
    
def regresion_linear(request, nidea):
    filtro = _queryset_filtrado(request)
    n = filtro.count()
    xy = nidea
    prueba = []
    for k,v in xy.items():
        for conteo in v:
            prueba.append(conteo)
    #comienza la formula
    lista_x = []
    lista_y = []
    for numero in range(0, len(prueba)):
        for k, v in xy.items():
            lista_x.append(v[numero][0])
            lista_y.append(v[numero][1])
            
    def cuadrado(n):
        return n** 2
    cuadrado_x = map(cuadrado, lista_x)
    suma_x = sum(lista_x)
    suma_y = sum(lista_y)
    m1 = n * (suma_x + suma_y) - (suma_x + suma_y) 
    m2 = n * sum(cuadrado_x) - (sum(lista_x))**2
    #Pendiente
    try:
        m = m1 / m2
    except:
        m = 0
    
    b1 = suma_y - m * suma_x
    #inteseccion
    try:
        b = b1 / n
    except:
        b = 0
    
    y1 = m * 0 + b
    y2 = m * 15 + b
    lineal = [[0,round(y1,2)]]
    lineal.append([15,round(y2,2)]) 
    
    return lineal
    
def distribucion(request, items):
    a = _queryset_filtrado(request)
    grafo = {}
    for i in Cultivos.objects.filter(id=items):
        key = slugify(i.nombre).replace('-', '_')
        query = a.filter(cultivosfinca__cultivos = i)
        for obj in query:
            cultivos_finca = obj.cultivosfinca_set.filter(cultivos__id=items)
            for datos in cultivos_finca:
                if not key in grafo.keys():
                    grafo[key] = [[datos.productivos], ]
                else:
                    grafo[key].append([datos.productivos])
    
    xy = grafo
    prueba = []
    for k,v in xy.items():
        for conteo in v:
            prueba.append(conteo)
    #comienza la formula
    lista_productividad = []

    for numero in range(0, len(prueba)):
        for k, v in xy.items():
            lista_productividad.append(v[numero][0])
    rangos = {}
    rango1 = 0
    rango2 = 0
    rango3 = 0
    rango4 = 0
    rango5 = 0
    rango6 = 0
    rango7 = 0
    rango8 = 0
    rango9 = 0
    rango10 = 0
    rango11 = 0
    rango12 = 0   
    for cantidad in lista_productividad:
        if cantidad > 0.1 and cantidad <= 5:
            rango1 += 1
        elif cantidad > 5.1 and cantidad <= 10:
            rango2 += 1
        elif cantidad > 10.1 and cantidad <= 15:
            rango3 += 1
        elif cantidad > 15.1 and cantidad <= 20:
            rango4 += 1  
        elif cantidad > 20.1 and cantidad <= 30:
            rango5 += 1
        elif cantidad > 30.1 and cantidad <= 40:
            rango6 += 1
        elif cantidad > 40.1 and cantidad <= 50:
            rango7 += 1
        elif cantidad > 50.1 and cantidad <= 60:
            rango8 += 1
        elif cantidad > 60.1 and cantidad <= 70:
            rango9 += 1
        elif cantidad > 70.1 and cantidad <= 80:
            rango10 += 1
        elif cantidad > 80.1:
            rango11 += 1
    suma_rangos = rango1 + rango2 + rango3 + rango4 + rango5 + rango6 + rango7 + rango8 + \
                  rango9 + rango10 + rango11 + rango12
           
    rangos = {'0.1 - 5':int(saca_porcentajes(rango1,suma_rangos)),
              '5.1 - 10':int(saca_porcentajes(rango2,suma_rangos)),
              '10.1 - 15':int(saca_porcentajes(rango3,suma_rangos)),
              '15.1 - 20':int(saca_porcentajes(rango4,suma_rangos)),
              '20.1 - 30':int(saca_porcentajes(rango5,suma_rangos)),
              '30.1 - 40':int(saca_porcentajes(rango6,suma_rangos)),
              '40.1 - 50':int(saca_porcentajes(rango7,suma_rangos)),
              '50.1 - 60':int(saca_porcentajes(rango8,suma_rangos)),
              '60.1 - 70':int(saca_porcentajes(rango9,suma_rangos)),
              '70.1 - 80':int(saca_porcentajes(rango10,suma_rangos)),
              'más de 80.1':int(saca_porcentajes(rango11,suma_rangos))}
              
    llaves = ('0.1 - 5','5.1 - 10','10.1 - 15','15.1 - 20','20.1 - 30','30.1 - 40',
              '40.1 - 50','50.1 - 60','60.1 - 70','70.1 - 80','más de 80.1')
    
    dict = {'rangos':rangos,'llaves':llaves}
    return dict


@session_required
def cultivos(request):
    '''tabla los cultivos y produccion'''
    a = _queryset_filtrado(request)
    num_familias = a.count()
    
    tabla = {}
    for i in Cultivos.objects.all():
        key = slugify(i.nombre).replace('-', '_')
        key2 = slugify(i.unidad).replace('-', '_')
        query = a.filter(cultivosfinca__cultivos = i)
        numero = query.count()
        totales = query.aggregate(total=Sum('cultivosfinca__total'))['total']
        consumo = query.aggregate(consumo=Sum('cultivosfinca__consumo'))['consumo']
        libre = query.aggregate(libre=Sum('cultivosfinca__venta_libre'))['libre']
        organizada =query.aggregate(organizada=Sum('cultivosfinca__venta_organizada'))['organizada']
        if numero > 0:
            tabla[key] = {'key2':key2,'numero':numero,'totales':totales,
                           'consumo':consumo,'libre':libre,'organizada':organizada}
    
    tabla2 = {}
    lista_pro = [19,2,4,5,9,20,15,13,22,12,18,3,8]
    productividad = 0
    for i in Cultivos.objects.filter(id__in=lista_pro):
        key = slugify(i.nombre).replace('-', '_')
        key2 = slugify(i.unidad).replace('-', '_')
        query = a.filter(cultivosfinca__cultivos = i)
        numero = query.count()
        area_total = query.aggregate(area_total=Sum('cultivosfinca__area'))['area_total']
        area_avg = query.aggregate(area_avg=Avg('cultivosfinca__area'))['area_avg']
        totales = query.aggregate(total=Sum('cultivosfinca__total'))['total']
        try:
            productividad = totales / area_total
        except:
            productividad = 0
        if numero > 0:
            tabla2[key] = {'key2':key2,'numero':numero,'area_total':area_total,
                       'area_avg':area_avg,'totales':totales,'productividad':productividad}
                       
    maiz = grafo_generic(request,12)
    frijol = grafo_generic(request,8)
    platano = grafo_generic(request,18)
    guineo = grafo_generic(request,9)
    cafe = grafo_generic(request,5)
    cacao = grafo_generic(request,4)
    ###################################
    regresion_maiz = regresion_linear(request,maiz['grafo'])
    regresion_frijol = regresion_linear(request,frijol['grafo'])
    regresion_platano = regresion_linear(request,platano['grafo'])
    regresion_guineo = regresion_linear(request,guineo['grafo'])
    regresion_cafe = regresion_linear(request,cafe['grafo'])
    regresion_cacao = regresion_linear(request,cacao['grafo'])
    ################################
    distribucion_maiz = distribucion(request,12)
    distribucion_frijol = distribucion(request,8)
    distribucion_platano = distribucion(request,18)
    distribucion_guineo = distribucion(request,9)
    distribucion_cafe = distribucion(request,5)
    distribucion_cacao = distribucion(request,4)
                                           
    return render_to_response('simas/cultivos.html',
                             locals(),
                             context_instance=RequestContext(request))

#Tabla Ingreso familiar y otros ingresos
def total_ingreso(request, numero):
    #******Variables***************
    a = _queryset_filtrado(request)
    num_familias = a.count()
    #******************************
    #*******calculos de las variables ingreso************
    tabla = {}
    for i in Rubros.objects.filter(categoria=numero):
        key = slugify(i.nombre).replace('-','_')
        key2 = slugify(i.unidad).replace('-','_')
        query = a.filter(ingresofamiliar__rubro = i)
        numero = query.count()
        cantidad = query.aggregate(cantidad=Sum('ingresofamiliar__cantidad'))['cantidad']
        precio = query.aggregate(precio=Avg('ingresofamiliar__precio'))['precio']
        ingreso = cantidad * precio if cantidad != None and precio != None else 0
        if numero > 0:
            tabla[key] = {'key2':key2,'numero':numero,'cantidad':cantidad,
                      'precio':precio,'ingreso':ingreso}

    return tabla

@session_required
def ingresos(request):
    '''tabla de ingresos'''
    #******Variables***************
    a = _queryset_filtrado(request)
    num_familias = a.count()
    #******************************
    #*******calculos de las variables ingreso************
    respuesta = {}
    respuesta['bruto']= 0
    respuesta['ingreso']=0
    respuesta['ingreso_total']=0
    respuesta['ingreso_otro']=0
    respuesta['brutoo'] = 0
    respuesta['total_neto'] = 0
    agro = total_ingreso(request,1)
    forestal = total_ingreso(request,2)
    grano_basico = total_ingreso(request,3)
    ganado_mayor = total_ingreso(request,4)
    patio = total_ingreso(request,5)
    frutas = total_ingreso(request,6)
    musaceas = total_ingreso(request,7)
    raices = total_ingreso(request,8)

    total_agro = 0
    c_agro = 0
    for k,v in agro.items():
        total_agro += round(v['ingreso'],1)
        if v['numero'] > 0:
            c_agro += 1
    total_forestal = 0
    c_forestal = 0
    for k,v in forestal.items():
        total_forestal += round(v['ingreso'],1)
        if v['numero'] > 0:
            c_forestal += 1
    total_basico = 0
    c_basico = 0
    for k,v in grano_basico.items():
        total_basico += round(v['ingreso'],1)
        if v['numero'] > 0:
            c_basico += 1
    total_ganado = 0
    c_ganado = 0
    for k,v in ganado_mayor.items():
        total_ganado += round(v['ingreso'],1)
        if v['numero'] > 0:
            c_ganado += 1
    total_patio = 0
    c_patio = 0
    for k,v in patio.items():
        total_patio += round(v['ingreso'],1)
        if v['numero'] > 0:
            c_patio += 1
    total_fruta = 0
    c_fruta = 0
    for k,v in frutas.items():
        total_fruta += round(v['ingreso'],1)
        if v['numero'] > 0:
            c_fruta += 1
    total_musaceas = 0
    c_musaceas = 0
    for k,v in musaceas.items():
        total_musaceas += round(v['ingreso'],1)
        if v['numero'] > 0:
            c_musaceas += 1
    total_raices = 0
    c_raices = 0
    for k,v in raices.items():
        total_raices += round(v['ingreso'],1)
        if v['numero'] > 0:
            c_raices += 1

    respuesta['ingreso'] = total_agro + total_forestal + total_basico + total_ganado + total_patio + total_fruta + total_musaceas + total_raices
    grafo = []
    grafo.append({'Agroforestales':int(total_agro),'Forestales':int(total_forestal),
                  'Granos_basicos':int(total_basico),'Ganado_mayor':int(total_ganado),
                  'Animales_de_patio':int(total_patio),'Hortalizas_y_frutas':int(total_fruta),
                  'Musaceas':int(total_musaceas),'Tuberculos_y_raices':int(total_raices)
                 })
                 
    cuantos = []
    cuantos.append({'Agroforestales':c_agro,'Forestales':c_forestal,'Granos_basicos':c_basico,
                  'Ganado_mayor':c_ganado,'Animales_de_patio':c_patio,
                  'Hortalizas_y_frutas':c_fruta,'Musaceas':c_musaceas,
                  'Tuberculos_y_raices':c_raices})

    #********* calculos de las variables de otros ingresos******
    matriz = {}
    for j in Fuentes.objects.all():
        key = slugify(j.nombre).replace('-','_')
        consulta = a.filter(otrosingresos__fuente = j)
        frecuencia = consulta.count()
        meses = consulta.aggregate(meses=Sum('otrosingresos__meses'))['meses']
        ingreso = consulta.aggregate(ingreso=Avg('otrosingresos__ingreso'))['ingreso']
        try:
            ingresototal = round(meses * ingreso,2)
        except:
            ingresototal = 0
        respuesta['ingreso_otro'] +=  ingresototal
        #ingresototal = consulta.aggregate(meses=Avg('otrosingresos__meses'))['meses'] * consulta.aggregate(ingreso=Avg('otrosingresos__ingreso'))['ingreso'] if meses != None and ingreso != None else 0
        #ingresototal = consulta.aggregate(total=Avg('otrosingresos__ingreso_total'))['total']
        matriz[key] = {'frecuencia':frecuencia,'meses':meses,
                       'ingreso':ingreso,'ingresototal':ingresototal}

    try:
        respuesta['bruto'] = round((respuesta['ingreso'] + respuesta['ingreso_otro']) / num_familias,2)
    except:
        pass
    respuesta['total_neto'] = round(respuesta['bruto'] * 0.6,2)

    return render_to_response('simas/ingreso.html',locals(),
                              context_instance=RequestContext(request))
@session_required
def ingresos2(request):
    '''tabla de ingresos'''
    #******Variables***************
    a = _queryset_filtrado(request)
    num_familias = a.count()
    #******************************
    #*******calculos de las variables ingreso************
    tabla = {}
    respuesta = {}
    respuesta['bruto']=[]
    respuesta['ingreso']=0
    respuesta['ingreso_total']=0
    respuesta['ingreso_otro']=0
    respuesta['brutoo'] = 0
    respuesta['total_neto'] = 0
    for i in Rubros.objects.all():
        key = slugify(i.nombre).replace('-','_')
        key2 = slugify(i.unidad).replace('-','_')
        query = a.filter(ingresofamiliar__rubro = i)
        numero = query.count()
        cantidad = query.aggregate(cantidad=Sum('ingresofamiliar__cantidad'))['cantidad']
        precio = query.aggregate(precio=Avg('ingresofamiliar__precio'))['precio']
        ingreso = cantidad * precio if cantidad != None and precio != None else 0
        respuesta['ingreso']= query.aggregate(cantidad=Sum('ingresofamiliar__cantidad'))['cantidad'] * query.aggregate(precio=Avg('ingresofamiliar__precio'))['precio'] if cantidad != None and precio != None else 0
        respuesta['ingreso_total'] +=  respuesta['ingreso']

        tabla[key] = {'key2':key2,'numero':numero,'cantidad':cantidad,
                      'precio':precio,'ingreso':ingreso}

    #********* calculos de las variables de otros ingresos******
    matriz = {}
    for j in Fuentes.objects.all():
        key = slugify(j.nombre).replace('-','_')
        consulta = a.filter(otrosingresos__fuente = j)
        frecuencia = consulta.count()
        meses = consulta.aggregate(meses=Avg('otrosingresos__meses'))['meses']
        ingreso = consulta.aggregate(ingreso=Avg('otrosingresos__ingreso'))['ingreso']
        ingresototal = consulta.aggregate(meses=Avg('otrosingresos__meses'))['meses'] * consulta.aggregate(ingreso=Avg('otrosingresos__ingreso'))['ingreso'] if meses != None and ingreso != None else 0
        respuesta['ingreso_otro'] +=  ingresototal
        #ingresototal = consulta.aggregate(total=Avg('otrosingresos__ingreso_total'))['total']
        matriz[key] = {'frecuencia':frecuencia,'meses':meses,
                       'ingreso':ingreso,'ingresototal':ingresototal}

    respuesta['brutoo'] = round((respuesta['ingreso_total'] + respuesta['ingreso_otro']) / num_familias,2)
    respuesta['total_neto'] = round(respuesta['brutoo'] * 0.6,2)

    return render_to_response('simas/ingreso.html',
                              {'tabla':tabla,'num_familias':num_familias,'matriz':matriz,
                              'respuesta':respuesta},
                              context_instance=RequestContext(request))

# Tabla equipo, infrestructura, herramientas y medio de transporte
@session_required
def equipos(request):
    '''tabla de equipos'''
    #******** variables globales***********
    a = _queryset_filtrado(request)
    num_familia = a.count()
    #*************************************

    #********** tabla de equipos *************
    tabla = {}
    totales = {}

    totales['numero'] = a.aggregate(numero=Count('propiedades__equipo'))['numero']
    totales['porciento_equipo'] = 100
    totales['cantidad_equipo'] = a.aggregate(cantidad=Sum('propiedades__cantidad_equipo'))['cantidad']
    totales['porciento_cantidad'] = 100

    for i in Equipos.objects.all():
        key = slugify(i.nombre).replace('-','_')
        query = a.filter(propiedades__equipo = i)
        frecuencia = query.count()
        por_equipo = saca_porcentajes(frecuencia, num_familia)
        equipo = query.aggregate(equipo=Sum('propiedades__cantidad_equipo'))['equipo']
        cantidad_pro = query.aggregate(cantidad_pro=Avg('propiedades__cantidad_equipo'))['cantidad_pro']
        tabla[key] = {'frecuencia':frecuencia, 'por_equipo':por_equipo,
                      'equipo':equipo,'cantidad_pro':cantidad_pro}

    #******** tabla de infraestructura *************
    tabla_infra = {}
    totales_infra = {}

    totales_infra['numero'] = a.aggregate(numero=Count('propiedades__infraestructura'))['numero']
    totales_infra['porciento_infra'] = 100
    totales_infra['cantidad_infra'] = a.aggregate(cantidad_infra=Sum('propiedades__cantidad_infra'))['cantidad_infra']
    totales_infra['por_cantidad_infra'] = 100

    for j in Infraestructuras.objects.all():
        key = slugify(j.nombre).replace('-','_')
        query = a.filter(propiedades__infraestructura = j)
        frecuencia = query.count()
        por_frecuencia = saca_porcentajes(frecuencia, num_familia)
        infraestructura = query.aggregate(infraestructura=Sum('propiedades__cantidad_infra'))['infraestructura']
        infraestructura_pro = query.aggregate(infraestructura_pro=Avg('propiedades__cantidad_infra'))['infraestructura_pro']
        tabla_infra[key] = {'frecuencia':frecuencia, 'por_frecuencia':por_frecuencia,
                             'infraestructura':infraestructura,
                             'infraestructura_pro':infraestructura_pro}

    #******************* tabla de herramientas ***************************
    herramienta = {}
    totales_herramientas = {}

    totales_herramientas['numero'] = a.aggregate(numero=Count('herramientas__herramienta'))['numero']
    totales_herramientas['porciento_herra'] = 100
    totales_herramientas['cantidad_herra'] = a.aggregate(cantidad=Sum('herramientas__numero'))['cantidad']
    totales_herramientas['porciento_herra'] = 100

    for k in NombreHerramienta.objects.all():
        key = slugify(k.nombre).replace('-','_')
        query = a.filter(herramientas__herramienta = k)
        frecuencia = query.count()
        por_frecuencia = saca_porcentajes(frecuencia, num_familia)
        herra = query.aggregate(herramientas=Sum('herramientas__numero'))['herramientas']
        por_herra = query.aggregate(por_herra=Avg('herramientas__numero'))['por_herra']
        herramienta[key] = {'frecuencia':frecuencia, 'por_frecuencia':por_frecuencia,
                            'herra':herra,'por_herra':por_herra}

    #*************** tabla de transporte ***********************
    transporte = {}
    totales_transporte = {}

    totales_transporte['numero'] = a.aggregate(numero=Count('transporte__transporte'))['numero']
    totales_transporte['porciento_trans'] = 100
    totales_transporte['cantidad_trans'] = a.aggregate(cantidad=Sum('transporte__numero'))['cantidad']
    totales_transporte['porciento_trans'] = 100

    for m in NombreTransporte.objects.all():
        key = slugify(m.nombre).replace('-','_')
        query = a.filter(transporte__transporte = m)
        frecuencia = query.count()
        por_frecuencia = saca_porcentajes(frecuencia, num_familia)
        trans = query.aggregate(transporte=Sum('transporte__numero'))['transporte']
        por_trans = query.aggregate(por_trans=Avg('transporte__numero'))['por_trans']
        transporte[key] = {'frecuencia':frecuencia,'por_frecuencia':por_frecuencia,
                           'trans':trans,'por_trans':por_trans}

    return render_to_response('simas/equipos.html', {'tabla':tabla,'totales':totales,
                              'num_familias':num_familia,'tabla_infra':tabla_infra,
                              'herramienta':herramienta,'transporte':transporte},
                               context_instance=RequestContext(request))

#Tabla Ahorro
@session_required
def ahorro_credito(request):
    ''' ahorro y credito'''
    #ahorro
    consulta = _queryset_filtrado(request)
    tabla_ahorro = []
    totales_ahorro = {}

    columnas_ahorro = ['Si', '%']

    for pregunta in AhorroPregunta.objects.all():
        #opciones solo si
        subquery = consulta.filter(ahorro__ahorro = pregunta, ahorro__respuesta = 1).count()
        tabla_ahorro.append([pregunta.nombre, subquery, saca_porcentajes(subquery, consulta.count(), False)])

    #credito
    tabla_credito= {}
    totales_credito= {}

    totales_credito['numero'] = consulta.count()
    totales_credito['porcentaje_num'] = 100

    recibe = consulta.filter(credito__recibe = 1).count()
    menos = consulta.filter(credito__desde = 1).count()
    mas = consulta.filter(credito__desde = 2).count()
    al_dia = consulta.filter(credito__dia= 1).count()

    tabla_credito['recibe'] = [recibe, saca_porcentajes(recibe, totales_credito['numero'])]
    tabla_credito['menos'] = [menos, saca_porcentajes(menos, totales_credito['numero'])]
    tabla_credito['mas'] = [mas, saca_porcentajes(mas, totales_credito['numero'])]
    tabla_credito['al_dia'] = [al_dia, saca_porcentajes(al_dia, totales_credito['numero'])]

    dicc = {'tabla_ahorro':tabla_ahorro, 'columnas_ahorro': columnas_ahorro,
            'totales_ahorro': totales_ahorro, 'tabla_credito': tabla_credito,
            'num_familias': consulta.count()}

    return render_to_response('simas/ahorro_credito.html', dicc,
                              context_instance=RequestContext(request))

#Tabla seguridad alimentaria
def alimentos(request,numero):
    #********variables globales****************
    a = _queryset_filtrado(request)
    num_familia = a.count()
    #******************************************
    tabla = {}

    for u in Alimentos.objects.filter(categoria=numero):
        key = slugify(u.nombre).replace('-','_')
        query = a.filter(seguridad__alimento = u)
        frecuencia = query.count()
        producen = query.filter(seguridad__alimento=u,seguridad__producen=1).aggregate(producen=Count('seguridad__producen'))['producen']
        por_producen = saca_porcentajes(producen, num_familia)
        compran = query.filter(seguridad__alimento=u,seguridad__compran=1).aggregate(compran=Count('seguridad__compran'))['compran']
        por_compran = saca_porcentajes(compran, num_familia)
        consumen = query.filter(seguridad__alimento=u,seguridad__consumen=1).aggregate(consumen=Count('seguridad__consumen'))['consumen']
        por_consumen = saca_porcentajes(consumen, num_familia)
        invierno = query.filter(seguridad__alimento=u,seguridad__consumen_invierno=1).aggregate(invierno=Count('seguridad__consumen_invierno'))['invierno']
        por_invierno = saca_porcentajes(invierno, num_familia)
        tabla[key] = {'frecuencia':frecuencia, 'producen':producen, 'por_producen':por_producen,
                      'compran':compran,'por_compran':por_compran,'consumen':consumen,
                      'por_consumen':int(por_consumen), 'invierno':invierno,
                      'por_invierno':int(por_invierno)}
    return tabla


@session_required
def seguridad_alimentaria(request):
    '''Seguridad Alimentaria'''
    #********variables globales****************
    a = _queryset_filtrado(request)
    num_familia = a.count()
    num_familias = num_familia
    #******************************************

    carbohidrato = alimentos(request,1)
    grasa = alimentos(request,2)
    minerales = alimentos(request,3)
    proteinas = alimentos(request,4)
    lista = []
    carbo = 0
    for k,v in carbohidrato.items():
        if v['producen'] > 0:
            carbo += 1

    gra = 0
    for k,v in grasa.items():
        if v['producen'] > 0:
            gra += 1

    mine = 0
    for k,v in minerales.items():
        if v['producen'] > 0:
            mine += 1

    prot = 0
    for k,v in proteinas.items():
        if v['producen'] > 0:
            prot += 1
    lista.append({'Carbohidrato':carbo,'Grasa':gra,'Minerales/Vitamina':mine,'Proteinas':prot})

    return render_to_response('simas/seguridad.html',locals(),
                               context_instance=RequestContext(request))

#tabla opciones de manejo
@session_required
def opcionesmanejo(request):
    '''Opciones de manejo agroecologico'''
    #********variables globales****************
    a = _queryset_filtrado(request)
    num_familia = a.count()
    #******************************************
    tabla = {}

    for k in ManejoAgro.objects.all():
        key = slugify(k.nombre).replace('-','_')
        query = a.filter(opcionesmanejo__uso = k)
        frecuencia = query.count()
        nada = query.filter(opcionesmanejo__uso=k,
                            opcionesmanejo__nivel=1).aggregate(nada=Count('opcionesmanejo__nivel'))['nada']
        por_nada = saca_porcentajes(nada, num_familia)
        poco = query.filter(opcionesmanejo__uso=k,
                            opcionesmanejo__nivel=2).aggregate(poco=Count('opcionesmanejo__nivel'))['poco']
        por_poco = saca_porcentajes(poco, num_familia)
        algo = query.filter(opcionesmanejo__uso=k,
                            opcionesmanejo__nivel=3).aggregate(algo=Count('opcionesmanejo__nivel'))['algo']
        por_algo = saca_porcentajes(algo, num_familia)
        bastante = query.filter(opcionesmanejo__uso=k,
                                opcionesmanejo__nivel=4).aggregate(bastante=Count('opcionesmanejo__nivel'))['bastante']
        por_bastante = saca_porcentajes(bastante, num_familia)

        tabla[key] = {'nada':nada,'poco':poco,'algo':algo,'bastante':bastante,
                      'por_nada':por_nada,'por_poco':por_poco,'por_algo':por_algo,
                      'por_bastante':por_bastante}
    tabla_escala = {}
    for u in ManejoAgro.objects.all():
        key = slugify(u.nombre).replace('-','_')
        query = a.filter(opcionesmanejo__uso = u)
        frecuencia = query.count()
        menor_escala = query.filter(opcionesmanejo__uso=u,
                                    opcionesmanejo__menor_escala=1).aggregate(menor_escala=
                                    Count('opcionesmanejo__menor_escala'))['menor_escala']
        menor_escala2 = query.filter(opcionesmanejo__uso=u,
                                     opcionesmanejo__menor_escala=2).aggregate(menor_escala2=
                                     Count('opcionesmanejo__menor_escala'))['menor_escala2']
        #total_menor = menor_escala + menor_escala2
        total_menor = menor_escala
        por_menor_escala = saca_porcentajes(total_menor,num_familia)
        # vamos ahora con la mayor escala

        mayor_escala = query.filter(opcionesmanejo__uso=u,
                                    opcionesmanejo__mayor_escala=1).aggregate(mayor_escala=
                                    Count('opcionesmanejo__mayor_escala'))['mayor_escala']
        mayor_escala2 = query.filter(opcionesmanejo__uso=u,
                                    opcionesmanejo__mayor_escala=2).aggregate(mayor_escala2=
                                    Count('opcionesmanejo__mayor_escala'))['mayor_escala2']
        #total_mayor = mayor_escala + mayor_escala2
        total_mayor = mayor_escala
        por_mayor_escala = saca_porcentajes(total_mayor, num_familia)
        tabla_escala[key] = {'menor_escala':menor_escala,'menor_escala2':menor_escala2,
                             'mayor_escala':mayor_escala,'mayor_escala2':mayor_escala2,
                             'por_menor_escala':por_menor_escala,'por_mayor_escala':por_mayor_escala}


    return render_to_response('simas/manejo_agro.html',{'tabla':tabla,
                              'num_familias':num_familia,'tabla_escala':tabla_escala},
                               context_instance=RequestContext(request))

#tabla uso de semilla
@session_required
def usosemilla(request):
    '''Uso de Semilla'''
    #********variables globales****************
    a = _queryset_filtrado(request)
    num_familia = a.count()
    #******************************************
    tabla = {}
    lista = []
    for k in Variedades.objects.all():
        key = slugify(k.variedad).replace('-','_')
        key2 = slugify(k.cultivo.cultivo).replace('-','_')
        query = a.filter(semilla__cultivo = k )
        frecuencia = query.count()
        frec = query.filter(semilla__cultivo=k).count()
        porce = saca_porcentajes(frec,num_familia)
        nativos = query.filter(semilla__cultivo=k,semilla__origen=1).aggregate(nativos=Count('semilla__origen'))['nativos']
        introducidos = query.filter(semilla__cultivo=k,semilla__origen=2).aggregate(introducidos=Count('semilla__origen'))['introducidos']
        suma_semilla = nativos + introducidos
        por_nativos = saca_porcentajes(nativos, suma_semilla)
        por_introducidos = saca_porcentajes(introducidos, suma_semilla)

        lista.append([key,key2,frec,porce,nativos,por_nativos,
                      introducidos,por_introducidos])

        tabla[key] = {'key2':key2,'frec':frec,'porce':porce,'nativos':nativos,'introducidos':introducidos,
                      'por_nativos':por_nativos,'por_introducidos':por_introducidos}

    return render_to_response('simas/semilla.html',{'tabla':tabla,'lista':lista,
                              'num_familias':num_familia},
                              context_instance=RequestContext(request))

#tabla suelos
@session_required
def suelos(request):
    '''Uso del suelos'''
    #********variables globales****************
    a = _queryset_filtrado(request)
    num_familia = a.count()
    #******************************************
    tabla_textura = {}

    #caracteristicas del terrenos
    for k in Textura.objects.all():
        key = slugify(k.nombre).replace('-','_')
        query = a.filter(suelo__textura = k)
        frecuencia = query.count()
        textura = query.filter(suelo__textura=k).aggregate(textura=Count('suelo__textura'))['textura']
        por_textura = saca_porcentajes(textura, num_familia)
        tabla_textura[key] = {'textura':textura,'por_textura':por_textura}

    #profundidad del terrenos
    tabla_profundidad = {}

    for u in Profundidad.objects.all():
        key = slugify(u.nombre).replace('-','_')
        query = a.filter(suelo__profundidad = u)
        frecuencia = query.count()
        profundidad = query.filter(suelo__profundidad=u).aggregate(profundidad=Count('suelo__profundidad'))['profundidad']
        por_profundidad = saca_porcentajes(profundidad, num_familia)
        tabla_profundidad[key] = {'profundidad':profundidad,'por_profundidad':por_profundidad}

    #profundidad del lombrices
    tabla_lombrices = {}

    for j in Densidad.objects.all():
        key = slugify(j.nombre).replace('-','_')
        query = a.filter(suelo__lombrices = j)
        frecuencia = query.count()
        lombrices = query.filter(suelo__lombrices=j).aggregate(lombrices=Count('suelo__lombrices'))['lombrices']
        por_lombrices = saca_porcentajes(lombrices, num_familia)
        tabla_lombrices[key] = {'lombrices':lombrices,'por_lombrices':por_lombrices}

     #Densidad
    tabla_densidad = {}

    for j in Densidad.objects.all():
        key = slugify(j.nombre).replace('-','_')
        query = a.filter(suelo__densidad = j)
        frecuencia = query.count()
        densidad = query.filter(suelo__densidad=j).aggregate(densidad=Count('suelo__densidad'))['densidad']
        por_densidad = saca_porcentajes(densidad, num_familia)
        tabla_densidad[key] = {'densidad':densidad,'por_densidad':por_densidad}

      #Pendiente
    tabla_pendiente = {}

    for j in Pendiente.objects.all():
        key = slugify(j.nombre).replace('-','_')
        query = a.filter(suelo__densidad = j)
        frecuencia = query.count()
        pendiente = query.filter(suelo__pendiente=j).aggregate(pendiente=Count('suelo__pendiente'))['pendiente']
        por_pendiente = saca_porcentajes(pendiente, num_familia)
        tabla_pendiente[key] = {'pendiente':pendiente,'por_pendiente':por_pendiente}

      #Drenaje
    tabla_drenaje = {}

    for j in Drenaje.objects.all():
        key = slugify(j.nombre).replace('-','_')
        query = a.filter(suelo__drenaje = j)
        frecuencia = query.count()
        drenaje = query.filter(suelo__drenaje=j).aggregate(drenaje=Count('suelo__drenaje'))['drenaje']
        por_drenaje = saca_porcentajes(drenaje, num_familia)
        tabla_drenaje[key] = {'drenaje':drenaje,'por_drenaje':por_drenaje}

    #Materia
    tabla_materia = {}

    for j in Densidad.objects.all():
        key = slugify(j.nombre).replace('-','_')
        query = a.filter(suelo__materia = j)
        frecuencia = query.count()
        materia = query.filter(suelo__materia=j).aggregate(materia=Count('suelo__materia'))['materia']
        por_materia = saca_porcentajes(materia, num_familia)
        tabla_materia[key] = {'materia':materia,'por_materia':por_materia}

    return render_to_response('simas/suelos.html',{'tabla_textura':tabla_textura,
                              'tabla_profundidad':tabla_profundidad,'tabla_densidad':tabla_densidad,
                              'tabla_lombrices':tabla_lombrices,'tabla_pendiente':tabla_pendiente,
                              'tabla_drenaje':tabla_drenaje,'tabla_materia':tabla_materia,
                              'num_familias':num_familia},
                               context_instance=RequestContext(request))

#tabla manejo de suelo
@session_required
def manejosuelo(request):
    ''' Manejo del suelos'''
    #********variables globales****************
    a = _queryset_filtrado(request)
    num_familia = a.count()
    #******************************************

    #Terrenos
    tabla_terreno = {}
    for j in Preparar.objects.all():
        key = slugify(j.nombre).replace('-','_')
        query = a.filter(manejosuelo__preparan = j)
        frecuencia = query.count()
        preparan = query.filter(manejosuelo__preparan=j).aggregate(preparan=Count('manejosuelo__preparan'))['preparan']
        por_preparan = saca_porcentajes(preparan, num_familia)
        tabla_terreno[key] = {'preparan':preparan,'por_preparan':por_preparan}

    #Tracción
    tabla_traccion = {}
    for j in Traccion.objects.all():
        key = slugify(j.nombre).replace('-','_')
        query = a.filter(manejosuelo__traccion = j)
        frecuencia = query.count()
        traccion = query.filter(manejosuelo__traccion=j).aggregate(traccion=Count('manejosuelo__traccion'))['traccion']
        por_traccion = saca_porcentajes(traccion, num_familia)
        tabla_traccion[key] = {'traccion':traccion,'por_traccion':por_traccion}

    #Fertilización
    tabla_fertilizacion = {}
    for j in Fertilizacion.objects.all():
        key = slugify(j.nombre).replace('-','_')
        query = a.filter(manejosuelo__fertilizacion = j)
        frecuencia = query.count()
        fertilizacion = query.filter(manejosuelo__fertilizacion=j).aggregate(fertilizacion=Count('manejosuelo__fertilizacion'))['fertilizacion']
        por_fertilizacion = saca_porcentajes(fertilizacion, num_familia)
        tabla_fertilizacion[key] = {'fertilizacion':fertilizacion,
                                    'por_fertilizacion':por_fertilizacion}

    #Tipo obra de conservación del suelo
    tabla_obra = {}
    for j in Conservacion.objects.all():
        key = slugify(j.nombre).replace('-','_')
        query = a.filter(manejosuelo__obra = j)
        frecuencia = query.count()
        obra = query.filter(manejosuelo__obra=j).aggregate(obra=Count('manejosuelo__obra'))['obra']
        por_obra = saca_porcentajes(obra, num_familia)
        tabla_obra[key] = {'obra':obra,'por_obra':por_obra}

    return render_to_response('simas/manejo_suelo.html',{'tabla_terreno':tabla_terreno,
                              'tabla_traccion':tabla_traccion,'tabla_fertilizacion':tabla_fertilizacion,
                              'tabla_obra':tabla_obra,'num_familias':num_familia},
                               context_instance=RequestContext(request))

#tabla finca vulnerable
def graves(request,numero):
    #********variables globales****************
    a = _queryset_filtrado(request)
    num_familia = a.count()
    #******************************************
    suma = 0
    for p in Graves.objects.all():
        fenomeno = a.filter(vulnerable__motivo__id=numero, vulnerable__respuesta=p).count()
        suma += fenomeno

    lista = []
    for x in Graves.objects.all():
        fenomeno = a.filter(vulnerable__motivo__id=numero, vulnerable__respuesta=x).count()
        porcentaje = round(saca_porcentajes(fenomeno,suma),2)
        lista.append([x.nombre,fenomeno,int(porcentaje)])
    return lista

#@session_required
def suma_graves(request,numero):
    #********variables globales****************
    a = _queryset_filtrado(request)
    num_familia = a.count()
    #******************************************
    suma = 0
    for p in Graves.objects.all():
        fenomeno = a.filter(vulnerable__motivo__id=numero, vulnerable__respuesta=p).count()
        suma += fenomeno
    return suma

#@session_required
def vulnerable(request):
    ''' Cuales son los Riesgos que hace las fincas vulnerables '''
    #********variables globales****************
    a = _queryset_filtrado(request)
    num_familia = a.count()
    num_familias = num_familia
    #******************************************

    #fenomenos naturales
    sequia = graves(request,1)
    total_sequia = suma_graves(request,1)
    inundacion = graves(request,2)
    total_inundacion = suma_graves(request,2)
    vientos = graves(request,3)
    total_vientos = suma_graves(request,3)
    deslizamiento = graves(request,4)
    total_deslizamiento = suma_graves(request,4)

    #Razones agricolas
    falta_semilla = graves(request,5)
    total_falta_semilla = suma_graves(request,5)
    mala_semilla = graves(request,6)
    total_mala_semilla = suma_graves(request,6)
    plagas = graves(request,7)
    total_plagas = suma_graves(request,7)

    #Razones de mercado
    bajo_precio = graves(request,8)
    total_bajo_precio = suma_graves(request,8)
    falta_venta = graves(request,9)
    total_falta_venta = suma_graves(request,9)
    estafa = graves(request,10)
    total_estafa = suma_graves(request,10)
    falta_calidad = graves(request,11)
    total_falta_calidad = suma_graves(request,11)

    #inversion
    falta_credito = graves(request,12)
    total_falta_credito = suma_graves(request,12)
    alto_interes = graves(request,13)
    total_alto_interes = suma_graves(request,13)

    return render_to_response('simas/vulnerable.html', locals(),
                              context_instance=RequestContext(request))

#tabla mitigacion de riesgos
@session_required
def mitigariesgos(request):
    ''' Mitigación de los Riesgos '''
    #********variables globales****************
    a = _queryset_filtrado(request)
    num_familia = a.count()
    #******************************************
    tabla = {}
    for j in PreguntaRiesgo.objects.all():
        key = slugify(j.nombre).replace('-','_')
        query = a.filter(riesgos__pregunta = j)
        mitigacion = query.filter(riesgos__pregunta=j, riesgos__respuesta=1).aggregate(mitigacion=Count('riesgos__pregunta'))['mitigacion']
        por_mitigacion = saca_porcentajes(mitigacion, num_familia)
        tabla[key] = {'mitigacion':mitigacion,'por_mitigacion':int(por_mitigacion)}

    return render_to_response('simas/mitigacion.html',{'tabla':tabla,
                              'num_familias':num_familia},
                               context_instance=RequestContext(request))

#GRAFICOS
@session_required
def organizacion_grafos(request, tipo):
    '''grafos de organizacion
       tipo puede ser: beneficio, miembro'''
    consulta = _queryset_filtrado(request)

    data = []
    legends = []
    if tipo == 'beneficio':
        for opcion in BeneficiosObtenido.objects.all():
            data.append(consulta.filter(organizaciongremial__beneficio=opcion).count())
            legends.append(opcion.nombre)
        return grafos.make_graph(data, legends,
                '¿Qué beneficios ha tenido por ser socio/a de la cooperativa, la asociación o empresa', return_json = True,
                type = grafos.PIE_CHART_3D)
    elif tipo == 'miembro':
        for opcion in SerMiembro.objects.all():
            data.append(consulta.filter(organizaciongremial__beneficio=opcion).count())
            legends.append(opcion.nombre)
        return grafos.make_graph(data, legends,
                'Porque soy o quiero ser miembro de la junta directiva o las comisiones', return_json = True,
                type = grafos.PIE_CHART_3D)
    elif tipo == 'estructura':
        for opcion in CHOICE_OPCION:
            data.append(consulta.filter(organizaciongremial__asumir_cargo=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends,
                'Si no es miembro de ninguna estructura ¿estaria interesado en asumir cargos?', return_json = True,
                type = grafos.PIE_CHART_3D)
    elif tipo == 'beneficiorganizado':
        for opcion in BeneficioOrgComunitaria.objects.all():
            data.append(consulta.filter(organizacioncomunitaria__cual_beneficio=opcion).count())
            legends.append(opcion.nombre)
        return grafos.make_graph(data, legends,
                '¿Cuáles son los beneficios de estar organizado', return_json = True,
                type = grafos.PIE_CHART_3D)
    elif tipo == 'norganizado':
        for opcion in NoOrganizado.objects.all():
            data.append(consulta.filter(organizacioncomunitaria__no_organizado=opcion).count())
            legends.append(opcion.nombre)
        return grafos.make_graph(data, legends,
                '¿Porqué no esta organizado?', return_json = True,
                type = grafos.PIE_CHART_3D)
    elif tipo == 'comunitario':
        for opcion in OrgComunitarias.objects.all():
            data.append(consulta.filter(organizacioncomunitaria__cual_organizacion=opcion).count())
            legends.append(opcion.nombre)
        return grafos.make_graph(data, legends,
                '¿A cual organizacion comunitaria pertenece', return_json = True,
                type = grafos.PIE_CHART_3D)
    else:
        raise Http404

@session_required
def agua_grafos_disponibilidad(request, tipo):
    '''Tipo: numero del 1 al 6 en CHOICE_FUENTE_AGUA'''
    consulta = _queryset_filtrado(request)
    data = []
    legends = []
    tipo = get_object_or_404(Fuente, id = int(tipo))
    for opcion in Disponibilidad.objects.all():
        data.append(consulta.filter(agua__disponible=opcion, agua__fuente = tipo).count())
        legends.append(opcion.nombre)
    titulo = 'Disponibilidad del agua en %s' % tipo.nombre
    return grafos.make_graph(data, legends,
            titulo, return_json = True,
            type = grafos.PIE_CHART_3D)

@session_required
def fincas_grafos(request, tipo):
    '''Tipo puede ser: tenencia, solares, propietario'''
    consulta = _queryset_filtrado(request)
    #CHOICE_TENENCIA, CHOICE_DUENO
    data = []
    legends = []
    if tipo == 'tenencia':
        for opcion in CHOICE_TENENCIA:
            data.append(consulta.filter(tenencia__parcela=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends,
                'Tenencia de las parcelas', return_json = True,
                type = grafos.PIE_CHART_3D)
    elif tipo == 'solares':
        for opcion in CHOICE_TENENCIA:
            data.append(consulta.filter(tenencia__solar=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends,
                'Tenencia de los solares', return_json = True,
                type = grafos.PIE_CHART_3D)
    elif tipo == 'propietario':
        for opcion in CHOICE_DUENO:
            data.append(consulta.filter(tenencia__dueno=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends,
                'Dueño de propiedad', return_json = True,
                type = grafos.PIE_CHART_3D)
    else:
        raise Http404

@session_required
def arboles_grafos(request, tipo):
    ''' graficos para los distintos tipos de arboles en las fincas
        Maderables, Forrajero, Energetico y Frutal
    '''
    #--- variables ---
    consulta = _queryset_filtrado(request)
    data = []
    legends = []
    #-----------------
    if tipo == 'maderable':
        for opcion in Maderable.objects.all():
            data.append(consulta.filter(existenciaarboles__maderable=opcion).count())
            legends.append(opcion.nombre)
        return grafos.make_graph(data, legends,
                'Tipo Maderable', return_json = True,
                type = grafos.PIE_CHART_3D)
    elif tipo == 'forrajero':
        for opcion in Forrajero.objects.all():
            data.append(consulta.filter(existenciaarboles__forrajero=opcion).count())
            legends.append(opcion.nombre)
        return grafos.make_graph(data, legends,
                'Tipo Forrajero', return_json = True,
                type = grafos.PIE_CHART_3D)
    elif tipo == 'energetico':
        for opcion in Energetico.objects.all():
            data.append(consulta.filter(existenciaarboles__energetico=opcion).count())
            legends.append(opcion.nombre)
        return grafos.make_graph(data, legends,
               'Tipo Energetico', return_json = True,
               type = grafos.PIE_CHART_3D)
    elif tipo == 'frutal':
        for opcion in Frutal.objects.all():
            data.append(consulta.filter(existenciaarboles__frutal=opcion).count())
            legends.append(opcion.nombre)
        return grafos.make_graph(data, legends,
               'Tipo Frutal', return_json = True,
               type = grafos.PIE_CHART_3D)
    else:
        raise Http404


@session_required
def grafo_manejosuelo(request, tipo):
    #--- variables ---
    consulta = _queryset_filtrado(request)
    data = []
    legends = []
    #-----------------
    if tipo == 'analisis':
        for opcion in CHOICE_OPCION:
            data.append(consulta.filter(manejosuelo__analisis=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends,
                '¿Realiza análisis de fertilidad del suelo', return_json = True,
                type = grafos.PIE_CHART_3D)
    elif tipo == 'practica':
        for opcion in CHOICE_OPCION:
            data.append(consulta.filter(manejosuelo__practica=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends,
                                 '¿Realiza práctica de conservación de suelo', return_json=True,
                                 type = grafos.PIE_CHART_3D)
    else:
        raise Http404


@session_required
def grafos_ingreso(request, tipo):
    ''' tabla sobre los ingresos familiares
    '''
    #------ varaibles ------
    consulta = _queryset_filtrado(request)
    data = []
    legends = []
    #-----------------------
    if tipo == 'vendio':
        for opcion in CHOICE_VENDIO:
            data.append(consulta.filter(ingresofamiliar__quien_vendio=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends,
                'A quien venden', return_json=True,
                type=grafos.PIE_CHART_3D)
    elif tipo == 'maneja':
        for opcion in CHOICE_MANEJA:
            data.append(consulta.filter(ingresofamiliar__maneja_negocio=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends,
                'Quien maneja negocio', return_json=True,
                type=grafos.PIE_CHART_3D)
    elif tipo == 'ingreso':
        for opcion in CHOICE_MANEJA:
            data.append(consulta.filter(otrosingresos__tiene_ingreso=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends,
                'Quien tiene los ingresos', return_json=True,
                type=grafos.PIE_CHART_3D)
    elif tipo == 'salario':
        for opcion in TipoTrabajo.objects.all():
            a = consulta.filter(otrosingresos__fuente__nombre__icontains="salarios",
                                        otrosingresos__tipo=opcion).count()
            if a > 0:
                data.append(a)
                legends.append(opcion)
        return grafos.make_graph(data, legends,
                'Tipos de salarios', return_json=True,
                type=grafos.PIE_CHART_3D)
    elif tipo == 'negocio':
        for opcion in TipoTrabajo.objects.all():
            a = consulta.filter(otrosingresos__fuente__nombre__icontains="negocios",
                                        otrosingresos__tipo=opcion).count()
            if a > 0:
                data.append(a)
                legends.append(opcion)
        return grafos.make_graph(data, legends,
                'Tipos de Negocios', return_json=True,
                type=grafos.PIE_CHART_3D)
    elif tipo == 'remesa':
        for opcion in TipoTrabajo.objects.all():
            a = consulta.filter(otrosingresos__fuente__nombre__icontains="remesas",
                                       otrosingresos__tipo=opcion).count()
            if a > 0:
                data.append(a)
                legends.append(opcion)
        return grafos.make_graph(data, legends,
                'Tipos de Remesas', return_json=True,
                type=grafos.PIE_CHART_3D)
    elif tipo == 'alquiler':
        for opcion in TipoTrabajo.objects.all():
            a = consulta.filter(otrosingresos__fuente__nombre__icontains="alquiler",
                                        otrosingresos__tipo=opcion).count()
            if a > 0:
                data.append(a)
                legends.append(opcion)
        return grafos.make_graph(data, legends,
                'Tipos de Alquiler', return_json=True,
                type=grafos.PIE_CHART_3D)
#    elif tipo == 'aportar':
#        #data.append[(consulta.filter(aporte__persona=opcion[0]).count())]
#        uno = consulta.filter(aporte__persona=1).count()
#        dos = consulta.filter(aporte__persona=2).count()
#        tres = consulta.filter(aporte__persona=3).count()
#        cuatro = consulta.filter(aporte__persona=4).count()
#
#        data = [[uno],[dos],[tres],[cuatro]]
#        legends = ['2-3','4-5','6-7','mas de 8']
#        message = "Aporte en la finca"
#        return grafos.make_graph(data, legends, message, multiline = True,
#                return_json = True, type = grafos.GROUPED_BAR_CHART_V)
    else:
        raise Http404

@session_required
def grafos_bienes(request, tipo):
    '''tabla de bienes'''
    #----- variables ------
    consulta = _queryset_filtrado(request)
    data = []
    legends = []
    #----------------------
    if tipo == 'tipocasa':
        for opcion in CHOICE_TIPO_CASA:
            data.append(consulta.filter(tipocasa__tipo=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends,
                'Tipos de casas', return_json = True,
                type = grafos.PIE_CHART_3D)
    elif tipo == 'tipopiso':
        for opcion in Piso.objects.all():
            data.append(consulta.filter(tipocasa__piso=opcion).count())
            legends.append(opcion.nombre)
        return grafos.make_graph(data, legends,
                'Tipo de pisos', return_json = True,
                type = grafos.PIE_CHART_3D)
    elif tipo == 'tipotecho':
        for opcion in Techo.objects.all():
            data.append(consulta.filter(tipocasa__techo=opcion).count())
            legends.append(opcion.nombre)
        return grafos.make_graph(data, legends,
                'Tipos de Techos', return_json = True,
                type = grafos.PIE_CHART_3D)
    elif tipo == 'ambiente':
        for opcion in CHOICE_AMBIENTE:
            data.append(consulta.filter(detallecasa__ambientes=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends,
               'Numeros de ambientes', return_json = True,
               type = grafos.PIE_CHART_3D)
    elif tipo == 'letrina':
        for opcion in CHOICE_OPCION:
            data.append(consulta.filter(detallecasa__letrina=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends,
                'Tiene letrina', return_json = True,
                type = grafos.PIE_CHART_3D)
    elif tipo == 'lavadero':
        for opcion in CHOICE_OPCION:
            data.append(consulta.filter(detallecasa__lavadero=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends,
               'Tiene lavadero', return_json = True,
               type = grafos.PIE_CHART_3D)

    else:
        raise Http404

@session_required
def ahorro_credito_grafos(request, tipo):
    '''Tipo puede ser: ahorro, uso, origen, satisfaccion'''
    consulta = _queryset_filtrado(request)
    data = []
    legends = []
    if tipo == 'ahorro': #ahorra a nombre de quien
        #choice_ahorro (5, hombre), (6, mujeres), (7,ambos)
        for numero in (5, 6, 7):
            #FIX: numero de la pregunta hardcored
            dato = consulta.filter(ahorro__ahorro=5, ahorro__respuesta = numero).count()
            data.append(dato)
            legends.append(CHOICE_AHORRO[numero - 1][1])
        return grafos.make_graph(data, legends,
                'A nombre de quien ahorra', return_json = True,
                type = grafos.PIE_CHART_3D)
    elif tipo == 'origen': #de donde viene el credito
        for origen in DaCredito.objects.all():
            data.append(consulta.filter(credito__quien_credito= origen).count())
            legends.append(origen.nombre)
        return grafos.make_graph(data, legends,
                'Origen del Crédito', return_json = True,
                type = grafos.PIE_CHART_3D)
    elif tipo == 'satisfaccion':
        for opcion in CHOICE_SATISFACCION:
            data.append(consulta.filter(credito__satisfaccion=opcion[0]).count())
            legends.append(opcion[1])
        return grafos.make_graph(data, legends,
                'Nivel de satisfacción con el crédito', return_json = True,
                type = grafos.PIE_CHART_3D)
    elif tipo == 'uso':
        for uso in OcupaCredito.objects.all():
            data.append(consulta.filter(credito__ocupa_credito = uso).count())
            legends.append(uso.nombre)
        return grafos.make_graph(data, legends,
                'Uso del Crédito', return_json = True,
                type = grafos.PIE_CHART_3D)
    else:
        raise Http404

#Los puntos en el mapa

def obtener_lista(request):
    if request.is_ajax():
        lista = []
        for objeto in Encuesta.objects.all():
            dicc = dict(nombre=objeto.nombre, id=objeto.id,
                        lon=float(objeto.comunidad.municipio.longitud) ,
                        lat=float(objeto.comunidad.municipio.latitud)
                        )
            lista.append(dicc)

        serializado = simplejson.dumps(lista)
        return HttpResponse(serializado, mimetype='application/json')

# Aca empieza el menu para los subindicadores :)

@session_required
def familia(request):
    '''Familias: aca van las familias con sus respectivos indicadores, educacion,
       salud, energia, agua.
    '''
    familias = _queryset_filtrado(request).count()
    return render_to_response('simas/familia.html',
                              {'num_familias':familias},
                              context_instance=RequestContext(request))

@session_required
def organizacion(request):
    '''Organizacion: aca van las organizaciones con sus respectivos indicadores,
       como son gremial y comunitaria.
    '''
    familias = _queryset_filtrado(request).count()
    return render_to_response('simas/organizacion.html',
                              {'num_familias':familias},
                              context_instance=RequestContext(request))

@session_required
def riesgo(request):
    '''Riesgos: aca van los riesgos con sus indicadores como son: vulnerabilidad
       en la finca asi como la mitigación de estos.
    '''
    familias = _queryset_filtrado(request).count()
    return render_to_response('simas/riesgos.html',
                              {'num_familias':familias},
                              context_instance=RequestContext(request))

@session_required
def suelo(request):
    '''Suelo: aca va el indicador de suelo con sus subindicadores: caracteristicas
       del terrreno y manejo del suelo
    '''
    familias = _queryset_filtrado(request).count()
    return render_to_response('simas/suelo.html',
                              {'num_familias':familias},
                              context_instance=RequestContext(request))

@session_required
def tenencias(request):
    '''Tenencia: aca van las tenencias con sus respectivos subindicadores:
       tenencia de la propiedad, documento legal, tierra etc.
    '''
    familias = _queryset_filtrado(request).count()
    return render_to_response('simas/tenencia.html',
                              {'num_familias':familias},
                              context_instance=RequestContext(request))

@session_required
def tierra(request):
    '''Tierra: aca va el indicador uso de tierra con su respectivos subindicadores:
       uso de la tierra, existencia de arboles y reforestacion.
    '''
    familias = _queryset_filtrado(request).count()
    return render_to_response('simas/tierra.html',
                              {'num_familias':familias},
                              context_instance=RequestContext(request))

##Para descargar xls un poco mas dinamico por modelo
def _queryset_filtrado_descarga(request):
    params = {}
    if 'fecha2' in request.session:
        params['year__in'] = request.session['fecha2']

    if request.session['departamento2']:
        if not request.session['municipio2']:
            municipios = Municipio.objects.filter(departamento__in=request.session['departamento2'])
            params['comunidad__municipio__in'] = municipios
        else:
            if request.session['comunidad2']:
                params['comunidad__in'] = request.session['comunidad2']
            else:
                params['comunidad__municipio__in'] = request.session['municipio2']

    if request.session['organizacion2']:
        params['organizacion__in'] = request.session['organizacion2']


    if 'duenio2' in  request.session:
        params['tenencia__dueno'] = request.session['duenio2']

    unvalid_keys = []
    for key in params:
        if not params[key]:
            unvalid_keys.append(key)

    for key in unvalid_keys:
        del params[key]

    return Encuesta.objects.filter(**params)


@session_required
def formulario_consulta_xls(request):
    if request.method == 'POST':
        form2 = ExportarMonitoreoForm(request.POST)
        if form2.is_valid():
            request.session['fecha2'] = form2.cleaned_data['fecha2']
            request.session['departamento2'] = form2.cleaned_data['departamento2']
            request.session['organizacion2'] = form2.cleaned_data['organizacion2']
            request.session['municipio2'] = form2.cleaned_data['municipio2']
            request.session['comunidad2'] = form2.cleaned_data['comunidad2']
            request.session['duenio2'] = form2.cleaned_data['dueno2']
            centinela = 1
    else:
        form2 = ExportarMonitoreoForm()
        centinela = 0
    return render_to_response('index_xls.html', locals(),
                              context_instance=RequestContext(request))



@session_required
def volcar_xls(request, modelo):
    #encuestas = _queryset_filtrado_descarga(request)
    encuestas = _queryset_filtrado(request)
    ayuda = modelo
    tiposexo = CHOICE_EDUCACION
    PEnergia = PreguntaEnergia.objects.all()
    usotierra = Uso.objects.all()
    reforestacion = Actividad.objects.all()
    animales = Animales.objects.all()
    cultivos = Cultivos.objects.all()
    manejo = ManejoAgro.objects.all()
    semilla = Variedades.objects.all()
    rubro = Rubros.objects.all()
    otrosingresos = TipoTrabajo.objects.all()
    equipo = Equipos.objects.all()
    herramienta = NombreHerramienta.objects.all()
    transporte = NombreTransporte.objects.all()
    ahorro = AhorroPregunta.objects.all()
    seguridad = Alimentos.objects.all()
    fenomeno = Fenomeno.objects.all()
    riesgos = PreguntaRiesgo.objects.all()

    resultados = []
    
    for encuesta in encuestas:
        filas = []
        filas.append(encuesta.fecha)
        filas.append(encuesta.nombre)
        filas.append(encuesta.cedula)
        filas.append(encuesta.get_sexo_display())
        filas.append(encuesta.finca)
        filas.append(encuesta.comunidad.municipio.departamento)
        filas.append(encuesta.comunidad.municipio)
        filas.append(encuesta.comunidad)
        filas.append(','.join(map(unicode, encuesta.organizacion.all().values_list(u'nombre',flat=True))))
        
        if modelo == '1':
            educacion = encuesta.educacion_set.all()
            for obj in educacion:
                filas.append(obj.get_sexo_display)
                filas.append(obj.total)
                filas.append(obj.no_leer)
                filas.append(obj.p_incompleta)
                filas.append(obj.p_completa)
                filas.append(obj.s_incompleta)
                filas.append(obj.bachiller)
                filas.append(obj.universitario)
                filas.append(obj.f_comunidad)
        
        if modelo == '2':
            salud = encuesta.salud_set.all()
            for obj in salud:
                filas.append(obj.get_sexo_display)
                filas.append(obj.b_salud)
                filas.append(obj.s_delicada)
                filas.append(obj.e_cronica)
                filas.append(obj.get_v_centro_display)
                filas.append(obj.get_v_medico_display)
                filas.append(obj.get_v_naturista_display)
                filas.append(obj.get_automedica_display)
        if modelo == '3':
            energia = encuesta.energia_set.all()
            for obj in energia:
                filas.append(obj.pregunta)
                filas.append(obj.get_respuesta_display)
        if modelo == '4':
            cocina = encuesta.cocina_set.all()
            for obj in cocina:
                filas.append(','.join(map(unicode, obj.utiliza.all().values_list(u'nombre',flat=True))))
        if modelo == '5':
            agua = encuesta.agua_set.all()
            for obj in agua:
                filas.append(','.join(map(unicode, obj.fuente.all().values_list(u'nombre',flat=True))))
                filas.append(','.join(map(unicode, obj.trata.all().values_list(u'nombre',flat=True))))
                filas.append(','.join(map(unicode, obj.disponible.all().values_list(u'nombre',flat=True))))
        if modelo == '6':
            gremial = encuesta.organizaciongremial_set.all()
            for obj in gremial:
                filas.append(','.join(map(unicode, obj.socio.all().values_list(u'nombre',flat=True))))
                filas.append(obj.desde_socio)
                filas.append(','.join(map(unicode, obj.beneficio.all().values_list(u'nombre',flat=True))))
                filas.append(obj.miembro_gremial)
                filas.append(obj.desde_miembro)
                filas.append(obj.capacitacion)
                filas.append(obj.desde_capacitacion)
                filas.append(','.join(map(unicode, obj.miembro_junta.all().values_list(u'nombre',flat=True))))
                filas.append(obj.asumir_cargo)
        if modelo == '7':
            comunitaria = encuesta.organizacioncomunitaria_set.all()
            for obj in comunitaria:
                filas.append(obj.numero)
                filas.append(obj.pertence)    
                filas.append(','.join(map(unicode, obj.cual_organizacion.all().values_list(u'nombre',flat=True))))
                filas.append(','.join(map(unicode, obj.cual_beneficio.all().values_list(u'nombre',flat=True))))
                filas.append(','.join(map(unicode, obj.no_organizado.all().values_list(u'nombre',flat=True))))
        if modelo == '8':
            usotierra = encuesta.usotierra_set.all()
            for obj in usotierra:
                filas.append(obj.tierra)
                filas.append(obj.area)
        if modelo == '9':
            arboles = encuesta.existenciaarboles_set.all()
            for obj in arboles:    
                filas.append(','.join(map(unicode, obj.maderable.all().values_list(u'nombre',flat=True))))
                filas.append(obj.cantidad_maderable)
                filas.append(','.join(map(unicode, obj.forrajero.all().values_list(u'nombre',flat=True))))
                filas.append(obj.cantidad_forrajero)
                filas.append(','.join(map(unicode, obj.energetico.all().values_list(u'nombre',flat=True))))
                filas.append(obj.cantidad_energetico)
                filas.append(','.join(map(unicode, obj.frutal.all().values_list(u'nombre',flat=True))))
                filas.append(obj.cantidad_frutal)
        if modelo == '10':
            reforestacion = encuesta.reforestacion_set.all()
            for obj in reforestacion:
                filas.append(obj.reforestacion)
                filas.append(obj.cantidad)
        if modelo == '11':
            animales = encuesta.animalesfinca_set.all()
            for obj in animales:
                filas.append(obj.animales)
                filas.append(obj.cantidad)
                filas.append(obj.produccion)
                filas.append(obj.total_produccion)
                filas.append(obj.consumo)
                filas.append(obj.venta_libre)
                filas.append(obj.venta_organizada)
        if modelo == '12':
            cultivos = encuesta.cultivosfinca_set.all()
            for obj in cultivos:
                filas.append(obj.cultivos)
                filas.append(obj.area)
                filas.append(obj.total)
                filas.append(obj.consumo)
                filas.append(obj.venta_libre)
                filas.append(obj.venta_organizada)
        if modelo == '13':
            manejo = encuesta.opcionesmanejo_set.all()
            for obj in manejo:
                filas.append(obj.uso)
                filas.append(obj.get_nivel_display())
                filas.append(obj.get_menor_escala_display())
                filas.append(obj.get_mayor_escala_display())
                filas.append(obj.volumen)
        if modelo == '14':
            semilla = encuesta.semilla_set.all()
            for obj in semilla:
                filas.append(obj.cultivo)
                filas.append(obj.get_origen_display())
        if modelo == '15':
            suelo = encuesta.suelo_set.all()
            for obj in suelo:
                filas.append(','.join(map(unicode, obj.textura.all().values_list(u'nombre',flat=True))))
                filas.append(','.join(map(unicode, obj.profundidad.all().values_list(u'nombre',flat=True))))
                filas.append(','.join(map(unicode, obj.lombrices.all().values_list(u'nombre',flat=True))))
                filas.append(','.join(map(unicode, obj.densidad.all().values_list(u'nombre',flat=True))))
                filas.append(','.join(map(unicode, obj.pendiente.all().values_list(u'nombre',flat=True))))
                filas.append(','.join(map(unicode, obj.drenaje.all().values_list(u'nombre',flat=True))))
                filas.append(','.join(map(unicode, obj.materia.all().values_list(u'nombre',flat=True))))
        if modelo == '16':
            manejosuelo = encuesta.manejosuelo_set.all()
            for obj in manejosuelo:
                filas.append(','.join(map(unicode, obj.preparan.all().values_list(u'nombre',flat=True))))
                filas.append(','.join(map(unicode, obj.traccion.all().values_list(u'nombre',flat=True))))
                filas.append(obj.get_analisis_display())
                filas.append(','.join(map(unicode, obj.fertilizacion.all().values_list(u'nombre',flat=True))))
                filas.append(obj.get_practica_display())
                filas.append(','.join(map(unicode, obj.obra.all().values_list(u'nombre',flat=True))))
        if modelo == '17':
            ingreso = encuesta.ingresofamiliar_set.all()
            for obj in ingreso:
                filas.append(obj.rubro)
                filas.append(obj.cantidad)
                filas.append(obj.precio)
                filas.append(obj.get_quien_vendio_display())
                filas.append(obj.get_maneja_negocio_display())
        if modelo == '18':
            otrosingreso = encuesta.otrosingresos_set.all()
            for obj in otrosingreso:
                filas.append(obj.fuente)
                filas.append(obj.tipo)
                filas.append(obj.meses)
                filas.append(obj.ingreso)
                filas.append(obj.get_tiene_ingreso_display())
        if modelo == '19':
            casa = encuesta.tipocasa_set.all()
            for obj in casa:
                filas.append(obj.get_tipo_display())
                filas.append(','.join(map(unicode, obj.piso.all().values_list(u'nombre',flat=True))))
                filas.append(','.join(map(unicode, obj.techo.all().values_list(u'nombre',flat=True))))
        if modelo == '20':
            detalle = encuesta.detallecasa_set.all()
            for obj in detalle:
                filas.append(obj.tamano)
                filas.append(obj.get_ambientes_display())
                filas.append(obj.get_letrina_display())
                filas.append(obj.get_lavadero_display())
        if modelo == '21':
            propiedades = encuesta.propiedades_set.all()
            for obj in propiedades:
                filas.append(obj.equipo)
                filas.append(obj.cantidad_equipo)
                filas.append(obj.infraestructura)
                filas.append(obj.cantidad_infra)
        if modelo == '22':
            herramientas = encuesta.herramientas_set.all()
            for obj in herramientas:
                filas.append(obj.herramienta)
                filas.append(obj.numero)
        if modelo == '23':
            transporte = encuesta.transporte_set.all()
            for obj in transporte:
                filas.append(obj.transporte)
                filas.append(obj.numero)
        if modelo == '24':
            ahorro = encuesta.ahorro_set.all()
            for obj in ahorro:
                filas.append(obj.ahorro)
                filas.append(obj.get_respuesta_display())
        if modelo == '25':
            credito = encuesta.credito_set.all()
            for obj in credito:
                filas.append(obj.get_recibe_display())
                filas.append(obj.get_desde_display())
                filas.append(','.join(map(unicode, obj.quien_credito.all().values_list(u'nombre',flat=True))))
                filas.append(','.join(map(unicode, obj.ocupa_credito.all().values_list(u'nombre',flat=True))))
                filas.append(obj.get_satisfaccion_display())
                filas.append(obj.get_dia_display())
        if modelo == '26':
            seguridad = encuesta.seguridad_set.all()
            for obj in seguridad:
                filas.append(obj.alimento)
                filas.append(obj.get_producen_display())
                filas.append(obj.get_compran_display())
                filas.append(obj.get_consumen_display())
                filas.append(obj.get_consumen_invierno_display())
        if modelo == '27':
            vulnerable = encuesta.vulnerable_set.all()
            for obj in vulnerable:
                filas.append(obj.motivo)
                filas.append(','.join(map(unicode, obj.respuesta.all().values_list(u'nombre',flat=True))))
        if modelo == '28':
            riesgos = encuesta.riesgos_set.all()
            for obj in riesgos:
                filas.append(obj.pregunta)
                filas.append(obj.get_respuesta_display())
        if modelo == '29':
            tenencia = encuesta.tenencia_set.all()
            for obj in tenencia:
                filas.append(obj.get_parcela_display())
                filas.append(obj.get_solar_display())
                filas.append(obj.get_dueno_display())
    
        resultados.append(filas)

    dict = {'resultados':resultados,'tiposexo':tiposexo, 'PEnergia':PEnergia, 
            'usotierra':usotierra,'reforestacion':reforestacion, 
            'animales':animales, 'cultivos':cultivos,
            'manejo':manejo, 'semilla':semilla, 'rubro':rubro, 
            'otrosingresos':otrosingresos, 'equipo':equipo, 'herramienta':herramienta,
            'transporte':transporte, 'ahorro':ahorro, 'seguridad':seguridad,
            'fenomeno':fenomeno, 'riesgos':riesgos, 'ayuda':ayuda}
    return dict

def spss_xls(request, modela):
    varia = modela
    dict = volcar_xls(request, modelo=varia)
    return write_xls('simas/spss.html', dict, 'spss.xls')

def write_xls(template_src, context_dict, filename):
    response = render_to_response(template_src, context_dict)
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel'
    response['Charset']='UTF-8'
    return response 

#TODO: completar esto
VALID_VIEWS = {
        'educacion': educacion,
        'salud': salud,
        'luz':luz,
        'agua': agua,
        'fincas':fincas,
        'arboles': arboles,
        'animales': animales,
        'cultivos': cultivos,
        'ingresos': ingresos,
        'equipos': equipos,
        'riesgo': riesgo,
        'tierra': tierra,
        'suelo': suelo,
        'suelos': suelos,
        'familia': familia,
        'gremial': gremial,
        'tenencias': tenencias,
        'usosemilla': usosemilla,
        'vulnerable': vulnerable,
        'manejosuelo': manejosuelo,
        'comunitario' : comunitario,
        'organizacion': organizacion,
        'mitigariesgos': mitigariesgos,
        'ahorro_credito': ahorro_credito,
        'opcionesmanejo': opcionesmanejo,
        'seguridad': seguridad_alimentaria,
        'general': generales,
        'consulta_xls':formulario_consulta_xls,
        #'exportar':spss_xls,
    }

# Vistas para obtener los municipios, comunidades, etc..

def get_munis(request):
    '''Metodo para obtener los municipios via Ajax segun los departamentos selectos'''
    ids = request.GET.get('ids', '')
    dicc = {}
    resultado = []
    if ids:
        lista = ids.split(',')
        for id in lista:
            try:
                departamento = Departamento.objects.get(pk=id)
                municipios = Municipio.objects.filter(departamento__id=departamento.pk).order_by('nombre')
                lista1 = []
                for municipio in municipios:
                    muni = {}
                    muni['id'] = municipio.pk
                    muni['nombre'] = municipio.nombre
                    lista1.append(muni)
                    dicc[departamento.nombre] = lista1
            except:
                pass

    #filtrar segun la organizacion seleccionada
    org_ids = request.GET.get('org_ids', '')
    if org_ids:
        lista = org_ids.split(',')
        municipios = [encuesta.municipio for encuesta in Encuesta.objects.filter(organizacion__id__in=lista)]
        #crear los keys en el dicc para evitar KeyError
        for municipio in municipios:
            dicc[municipio.departamento.nombre] = []

        #agrupar municipios por departamento padre
        for municipio in municipios:
            muni = {'id': municipio.id, 'nombre': municipio.nombre}
            if not muni in dicc[municipio.departamento.nombre]:
                dicc[municipio.departamento.nombre].append(muni)

    resultado.append(dicc)

    return HttpResponse(simplejson.dumps(resultado), mimetype='application/json')

def get_comunies(request):
    ids = request.GET.get('ids', '')
    if ids:
        lista = ids.split(',')
    results = []
    comunies = Comunidad.objects.filter(municipio__pk__in=lista).order_by('nombre').values('id', 'nombre')

    return HttpResponse(simplejson.dumps(list(comunies)), mimetype='application/json')

def get_organi(request):
    ids = request.GET.get('ids', '')
    if ids:
        lista = ids.split(',')
#    municipios = Municipio.objects.filter(departamento__pk__in=lista)
#    orgs_id_list = [encuesta.organizacion.all().values_list('id', flat=True) for encuesta in Encuesta.objects.filter(comunidad__municipio__in=municipios)]
#    print 'MMMMMMMMM'
#    print orgs_id_list
#    organizaciones = Organizaciones.objects.filter(pk__in=orgs_id_list).order_by('nombre').values('id', 'nombre')
    organizaciones = Organizaciones.objects.filter(departamento__id__in = lista).order_by('nombre').values('id', 'nombre')


    return HttpResponse(simplejson.dumps(list(organizaciones)), mimetype='application/json')

######viejo codigo#############################

def get_municipios(request, departamento):
    municipios = Municipio.objects.filter(departamento = departamento)
    lista = [(municipio.id, municipio.nombre) for municipio in municipios]
    return HttpResponse(simplejson.dumps(lista), mimetype='application/javascript')

def get_organizacion(request, departamento):
    organizaciones = Organizaciones.objects.filter(departamento = departamento)
    lista = [(organizacion.id, organizacion.nombre) for organizacion in organizaciones]
    return HttpResponse(simplejson.dumps(lista), mimetype='application/javascript')

def get_comunidad(request, municipio):
    comunidades = Comunidad.objects.filter(municipio = municipio )
    lista = [(comunidad.id, comunidad.nombre) for comunidad in comunidades]
    return HttpResponse(simplejson.dumps(lista), mimetype='application/javascript')

# Funciones utilitarias para cualquier proposito

def saca_porcentajes(values):
    """sumamos los valores y devolvemos una lista con su porcentaje"""
    total = sum(values)
    valores_cero = [] #lista para anotar los indices en los que da cero el porcentaje
    for i in range(len(values)):
        porcentaje = (float(values[i])/total)*100
        values[i] = "%.2f" % porcentaje + '%'
    return values

def saca_porcentajes(dato, total, formato=True):
    '''Si formato es true devuelve float caso contrario es cadena'''
    if dato != None:
        try:
            porcentaje = (dato/float(total)) * 100 if total != None or total != 0 else 0
        except:
            return 0
        if formato:
            return porcentaje
        else:
            return '%.2f' % porcentaje
    else:
        return 0

def calcular_positivos(suma, numero, porcentaje=True):
    '''Retorna el porcentaje de positivos'''
    try:
        positivos = (numero * 2) - suma
        if porcentaje:
            return '%.2f' % saca_porcentajes(positivos, numero)
        else:
            return positivos
    except:
        return 0

def calcular_negativos(suma, numero, porcentaje = True):
    positivos = calcular_positivos(suma, numero, porcentaje)
    if porcentaje:
        return 100 - float(positivos)
    else:
        return numero - positivos

#aca va ir la parte donde saldra las csv filtrados
#from django.db.models.loading import get_model
#import unicodecsv

# @session_required
# def volcar_csv(request):
#     qs = _queryset_filtrado(request)
#     opts = qs.model._meta
#     print dir(qs.model)
#     # for obj in qs.model.manejosuelo_set:
#     #     print obj
#     response = HttpResponse(mimetype='text/csv')
#     response['Content-Disposition'] = 'attachment;filename=export.csv'
#     writer = unicodecsv.writer(response, encoding='utf-8')
#     field_names = [field.name for field in opts.fields]
#     #print field_names
#     writer.writerow(field_names)

#     # escribimos las filas
#     for obj in qs:
#         writer.writerow([getattr(obj, field) for field in field_names])
#     return response
