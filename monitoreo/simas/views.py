# -*- coding: utf-8 -*-
from django.http import Http404, HttpResponse
from django.template.defaultfilters import slugify
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.generic.simple import direct_to_template
from django.utils import simplejson
from django.db.models import Sum, Count, Avg
from django.core.exceptions import ViewDoesNotExist

from simas.models import *
from indicador01.models import *
from indicador02.models import *
from indicador05.models import *
from indicador06.models import *
from indicador07.models import *
from indicador08.models import *
from indicador09.models import *
from indicador10.models import *
from indicador11.models import *
from indicador12.models import *
from indicador13.models import *
from indicador14.models import *
from indicador15.models import *
from indicador16.models import *
from indicador17.models import *
from indicador18.models import *
from indicador19.models import *
from indicador20.models import *

from decorators import session_required
from datetime import date
from forms import *
from lugar.models import *
from decimal import Decimal
#from utils import grafos
#from utils import *

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
    anio = int(request.session['fecha'])
    #diccionario de parametros del queryset
    params = {}
    if 'fecha' in request.session:
        params['fecha__year'] = anio

        if 'departamento' in request.session:
            #incluye municipio y comunidad
            if request.session['municipio']:
                if 'comunidad' in request.session:
                    params['encuesta__comunidad'] = request.session['comunidad']
                else:
                    params['encuesta__comunidad__municipio'] = request.session['municipio']
            else:
                params['encuesta__comunidad__municipio__departamento'] = request.session['departamento']

        if 'cooperativa' in request.session:
            params['encuesta__organizacion'] = request.session['organizacion']

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
    if request.method == 'POST':
        mensaje = None
        form = MonitoreoForm(request.POST)
        if form.is_valid():
            organizacion = form.cleaned_data['organizacion']
            request.session['organizacion'] = organizacion
            request.session['fecha'] = form.cleaned_data['fecha']
            request.session['departamento'] = form.cleaned_data['departamento']
            try:
                municipio = Municipio.objects.get(id=form.cleaned_data['municipio']) 
            except:
                municipio = None
            try:
                comunidad = Comunidad.objects.get(id=form.cleaned_data['comunidad'])
                
            except:
                comunidad = None

            request.session['municipio'] = municipio 
            request.session['comunidad'] = comunidad
            request.session['socio'] = form.cleaned_data['socio']
            request.session['desde'] = form.cleaned_data['desde']
            request.session['duenio'] = form.cleaned_data['dueno']

            mensaje = "Todas las variables estan correctamente :)"
            request.session['activo'] = True
            centinela = 1 #Variable para aparecer el menu de indicadores a lado del formulario
    else:
        form = MonitoreoForm()
        mensaje = "Existen alguno errores"
        centinela = 0
    dict = {'form': form,'user': request.user,'centinela':centinela}
    return render_to_response('simas/inicio.html', dict,
                              context_instance=RequestContext(request))        
        
#-------------------------------------------------------------------------------

def index(request):

    return direct_to_template(request, 'index.html')        
        
#-------------------------------------------------------------------------------

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
    
    for e in CHOICE_EDUCACION:
        objeto = a.filter(educacion__sexo = e[0]).aggregate(num_total = Sum('educacion__total'),
                no_leer = Sum('educacion__no_leer'), 
                p_incompleta = Sum('educacion__p_incompleta'), 
                p_completa = Sum('educacion__p_completa'), 
                s_incompleta = Sum('educacion__s_incompleta'),
                bachiller = Sum('educacion__bachiller'), 
                universitario = Sum('educacion__universitario'),
                f_comunidad = Sum('educacion__f_comunidad'))
        fila = [e[1], objeto['num_total'],
                saca_porcentajes(objeto['no_leer'], objeto['num_total'], False),
                saca_porcentajes(objeto['p_incompleta'], objeto['num_total'], False),
                saca_porcentajes(objeto['p_completa'], objeto['num_total'], False),
                saca_porcentajes(objeto['s_incompleta'], objeto['num_total'], False),
                saca_porcentajes(objeto['bachiller'], objeto['num_total'], False),
                saca_porcentajes(objeto['universitario'], objeto['num_total'], False),
                saca_porcentajes(objeto['f_comunidad'], objeto['num_total'], False)]
        tabla_educacion.append(fila)
    
    return render_to_response('simas/educacion.html', {'tabla_educacion':tabla_educacion,
                                  'num_familias':num_familias},
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
                    saca_porcentajes(resultados, total_tiene_luz, False)]
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

    totales['numero'] = consulta.count() 
    totales['porcentaje_num'] = 100
    totales['manzanas'] = consulta.aggregate(area=Sum('usotierra__area'))['area']
    totales['porcentaje_mz'] = 100

    for uso in Uso.objects.all():
        key = slugify(uso.nombre).replace('-', '_')
        query = consulta.filter(usotierra__tierra = uso)
        numero = query.count()
        porcentaje_num = saca_porcentajes(numero, totales['numero'])
        manzanas = query.aggregate(area = Sum('usotierra__area'))['area']
        porcentaje_mz = saca_porcentajes(manzanas, totales['manzanas'])
        tabla[key] = {'numero': numero, 'porcentaje_num': porcentaje_num,
                      'manzanas': manzanas, 'porcentaje_mz': porcentaje_mz}

    
    return render_to_response('simas/fincas.html', 
                              {'tabla':tabla, 'totales': totales,
                              'num_familias': consulta.count()},
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
        producto = AnimalesFinca.objects.filter(animales = animal)[0].produccion
        porcentaje_num = saca_porcentajes(numero, totales['numero'], False)
        animales = query.aggregate(cantidad = Sum('animalesfinca__cantidad'),
                                   venta_libre = Sum('animalesfinca__venta_libre'),
                                   venta_organizada = Sum('animalesfinca__venta_organizada'),
                                   consumo = Sum('animalesfinca__consumo'),
                                   produccion = Sum('animalesfinca__total_produccion'))
        try:
            animal_familia = animales['cantidad']/float(numero) 
        except:
            animal_familia = 0
        animal_familia = "%.2f" % animal_familia
        tabla.append([animal.nombre, numero, porcentaje_num,
                      animales['cantidad'], animal_familia])
        tabla_produccion.append([animal.nombre, animales['cantidad'], 
                                 producto.nombre, producto.unidad, 
                                 animales['produccion'], animales['consumo'], 
                                 animales['venta_libre'], animales['venta_organizada']])

    return render_to_response('simas/animales.html', 
                              {'tabla':tabla, 'totales': totales, 
                               'num_familias': consulta.count(),
                               'tabla_produccion': tabla_produccion},
                              context_instance=RequestContext(request))
                              
#Tabla Cultivos
@session_required
def cultivos(request):
    '''tabla los cultivos y produccion'''
    #******Variables***************
    a = _queryset_filtrado(request)
    num_familias = a.count()
    #******************************
    #**********calculosdelasvariables*****
    tabla = {} 
    for i in Cultivos.objects.all():
        key = slugify(i.nombre).replace('-', '_')
        key2 = slugify(i.unidad).replace('-', '_')
        query = a.filter(cultivosfinca__cultivos = i)
        totales = query.aggregate(total=Sum('cultivosfinca__total'))['total']
        consumo = query.aggregate(consumo=Sum('cultivosfinca__consumo'))['consumo']
        libre = query.aggregate(libre=Sum('cultivosfinca__venta_libre'))['libre']
        organizada =query.aggregate(organizada=Sum('cultivosfinca__venta_organizada'))['organizada']
        tabla[key] = {'key2':key2,'totales':totales,'consumo':consumo,'libre':libre,'organizada':organizada}
    #*******************************************
    return render_to_response('simas/cultivos.html',
                             {'tabla':tabla,'num_familias':num_familias},
                             context_instance=RequestContext(request))  

#Tabla Ingreso familiar y otros ingresos
@session_required
def ingresos(request):
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
@session_required
def seguridad_alimentaria(request):
    '''Seguridad Alimentaria'''
    #********variables globales****************
    a = _queryset_filtrado(request)
    num_familia = a.count()
    #******************************************
    tabla = {}
    
    for u in Alimentos.objects.all():
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
                      'por_consumen':por_consumen, 'invierno':invierno,
                      'por_invierno':por_invierno}
                     
                      
    return render_to_response('simas/seguridad.html',{'tabla':tabla,
                              'num_familias':num_familia},
                               context_instance=RequestContext(request))                         
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
        'ahorro_credito': ahorro_credito,
        'seguridad_alimentaria': seguridad_alimentaria,
            }
        
# Vistas para obtener los municipios, comunidades, etc..

def get_municipios(request, departamento):
    municipios = Municipio.objects.filter(departamento = departamento)
    lista = [(municipio.id, municipio.nombre) for municipio in municipios]
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
 
