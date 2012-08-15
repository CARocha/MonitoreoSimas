# -*- coding: UTF-8 -*-

from django.contrib import admin
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

class EducacionInline(admin.TabularInline):
    model = Educacion
    extra = 1
    max_num = 6
    
class SaludInline(admin.TabularInline):
    model = Salud
    extra = 1
    max_num = 6
    
class EnergiaInline(admin.TabularInline):
    model = Energia
    extra = 1
    max_num = 6
    
class CocinaInline(admin.TabularInline):
    model = Cocina
    extra = 1
    max_num = 1
    can_delete = True
    
class AguaInline(admin.TabularInline):
    model = Agua
    extra = 1
    max_num = 1
    can_delete = True
    
class OrganizacionGremialInline(admin.TabularInline):
    model = OrganizacionGremial
    fields = ['socio', 'desde_socio','beneficio', 'miembro_gremial', 
              'desde_miembro', 'capacitacion','desde_capacitacion',
              'miembro_junta', 'asumir_cargo']
    extra = 1
    max_num = 1
    can_delete = True
    
class OrganizacionComunitariaInline(admin.TabularInline):
    model = OrganizacionComunitaria
    fields = ['numero', 'pertence', 'cual_organizacion', 
              'cual_beneficio', 'no_organizado']
    extra = 1
    max_num = 1
    can_delete = True
    
class TenenciaInline(admin.TabularInline):
    model = Tenencia
    extra = 1
    max_num = 1
    can_delete = True
    
class UsoTierraInline(admin.TabularInline):
    model = UsoTierra
    extra = 1
    max_num = 8
    can_delete = True
    
class ExistenciaArbolesInline(admin.TabularInline):
    model = ExistenciaArboles
    fields = ['maderable', 'cantidad_maderable', 'forrajero', 'cantidad_forrajero',
              'energetico', 'cantidad_energetico', 'frutal', 'cantidad_frutal']
    extra = 1
    max_num = 1
    can_delete = True
    
class ReforestacionInline(admin.TabularInline):
    model = Reforestacion
    extra = 1
    can_delete = True
    
class AnimalesFincaInline(admin.TabularInline):
    model = AnimalesFinca
    extra = 1
    can_delete = True
    
class CultivosFincaInline(admin.TabularInline):
    model = CultivosFinca
    extra = 1
    can_delete = True
    
class OpcionesManejoInline(admin.TabularInline):
    model= OpcionesManejo
    extra = 1
    can_delete = True
    
class SemillaInline(admin.TabularInline):
    model = Semilla
    extra = 1
    can_delete = True
    
class SueloInline(admin.TabularInline):
    model = Suelo
    extra = 1
    max_num = 1
    can_delete = True
    
class ManejoSueloInline(admin.TabularInline):
    model = ManejoSuelo
    fields = ['preparan','traccion','analisis','fertilizacion',
              'practica','obra']
    extra = 1
    max_num = 1
    can_delete = True
    
class IngresoFamiliarInline(admin.TabularInline):
    model = IngresoFamiliar
    extra = 1
    can_delete = True
    
class OtrosIngresosInline(admin.TabularInline):
    model = OtrosIngresos
    extra = 1
    can_delete = True
    
class TipoCasaInline(admin.TabularInline):
    model = TipoCasa
    extra = 1
    max_num = 1
    can_delete = True
    
class DetalleCasaInline(admin.TabularInline):
    model = DetalleCasa
    extra = 1
    max_num = 1
    can_delete = True
    
class PropiedadesInline(admin.TabularInline):
    model = Propiedades
    extra = 1
    can_delete = True
    
class HerramientasInline(admin.TabularInline):
    model = Herramientas
    extra = 1
    can_delete = True
    
class TransporteInline(admin.TabularInline):
    model = Transporte
    extra = 1
    can_delete = True
    
class AhorroInline(admin.TabularInline):
    model = Ahorro
    extra = 1
    can_delete = True
    
class CreditoInline(admin.TabularInline):
    model = Credito
    fields = ['recibe','desde','quien_credito','ocupa_credito',
              'satisfaccion','dia']
    extra = 1
    max_num = 1
    can_delete = True
    
class SeguridadInline(admin.TabularInline):
    model = Seguridad
    extra = 1
    can_delete = True
    
class VulnerableInline(admin.TabularInline):
    model = Vulnerable
    extra = 1
    can_delete = True
    
class RiesgosInline(admin.TabularInline):
    model = Riesgos
    extra = 1
    can_delete = True
   
class EncuestaAdmin(admin.ModelAdmin):
    def queryset(self, request):
        if request.user.is_superuser:
            return Encuesta.objects.all()
        return Encuesta.objects.filter(user=request.user)

#    def get_form(self, request, obj=None, ** kwargs):
#        if request.user.is_superuser:
#            form = super(EncuestaAdmin, self).get_form(self, request, ** kwargs)
#        else:
#            form = super(EncuestaAdmin, self).get_form(self, request, ** kwargs)
#            form.base_fields['user'].queryset = User.objects.filter(pk=request.user.pk)
#        return form
        
    save_on_top = True
    actions_on_top = True
    inlines = [EducacionInline, SaludInline, EnergiaInline, CocinaInline,
               AguaInline, OrganizacionGremialInline, OrganizacionComunitariaInline,
               TenenciaInline, UsoTierraInline, ExistenciaArbolesInline,
               ReforestacionInline, AnimalesFincaInline, CultivosFincaInline,
               OpcionesManejoInline, SemillaInline, SueloInline, ManejoSueloInline,
               IngresoFamiliarInline, OtrosIngresosInline, TipoCasaInline,
               DetalleCasaInline, PropiedadesInline, HerramientasInline,
               TransporteInline, AhorroInline, CreditoInline, SeguridadInline,
               VulnerableInline, RiesgosInline,
               ]
    list_display = ('nombre', 'finca', 'comunidad')
    list_filter = ['comunidad', 'organizacion']
    search_fields = ['nombre', 'comunidad__nombre', 'organizacion__nombre']
    date_hierarchy = 'fecha'
               
admin.site.register(Encuesta, EncuestaAdmin)

#-------------------------------------------

admin.site.register(Recolector)
admin.site.register(Organizaciones)
admin.site.register(PreguntaEnergia)
admin.site.register(Fuente)
admin.site.register(Tratamiento)
admin.site.register(Disponibilidad)
admin.site.register(OrgGremiales)
admin.site.register(BeneficiosObtenido)
admin.site.register(SerMiembro)
admin.site.register(OrgComunitarias)
admin.site.register(BeneficioOrgComunitaria)
admin.site.register(NoOrganizado)
admin.site.register(Uso)
admin.site.register(Maderable)
admin.site.register(Forrajero)
admin.site.register(Energetico)
admin.site.register(Frutal)
admin.site.register(Actividad)
admin.site.register(Animales)
admin.site.register(ProductoAnimal)
#admin.site.register(Cultivos)
admin.site.register(ManejoAgro)
admin.site.register(CultivosVariedad)
admin.site.register(Variedades)
admin.site.register(Textura)
admin.site.register(Profundidad)
admin.site.register(Densidad)
admin.site.register(Pendiente)
admin.site.register(Drenaje)
admin.site.register(Preparar)
admin.site.register(Traccion)
admin.site.register(Fertilizacion)
admin.site.register(Conservacion)
admin.site.register(Rubros)
admin.site.register(Fuentes)
admin.site.register(TipoTrabajo)
admin.site.register(Piso)
admin.site.register(Techo)
admin.site.register(Equipos)
admin.site.register(Infraestructuras)
admin.site.register(NombreHerramienta)
admin.site.register(NombreTransporte)
admin.site.register(DaCredito)
admin.site.register(OcupaCredito)
admin.site.register(Alimentos)
admin.site.register(PreguntaRiesgo)
admin.site.register(Causa)
admin.site.register(Fenomeno)
admin.site.register(Graves)
admin.site.register(AhorroPregunta)
admin.site.register(TipoCocina)
