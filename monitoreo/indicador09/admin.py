from django.contrib import admin
from monitoreo.simas.models import *
from monitoreo.indicador09.models import *

class CultivosAdmin(admin.ModelAdmin):
	list_display = ('cultivos','area','total','productivos','nombre_encuestado',)
	list_filter = ('cultivos',)

admin.site.register(CultivosFinca, CultivosAdmin)
admin.site.register(Cultivos)