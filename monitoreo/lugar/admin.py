from django.contrib import admin
from lugar.models import *

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter = ['nombre']
    prepopulated_fields = {"slug": ("nombre",)}
    search_fields = ['nombre']

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ['nombre','departamento']
    list_filter = ['departamento']
    search_fields = ['nombre']
    prepopulated_fields = {"slug": ("nombre",)}

class ComunidadAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'municipio']
    list_filter = ['municipio']
    search_fields = ['nombre']

#class MicrocuencaAdmin(admin.ModelAdmin):
#    list_display = ['nombre']
#    search_fields = ['nombre']

admin.site.register(Departamento,DepartamentoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Comunidad, ComunidadAdmin)
#admin.site.register(Microcuenca, MicrocuencaAdmin)




