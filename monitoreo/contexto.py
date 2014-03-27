from indicador01.models import CHOICE_EDUCACION, PreguntaEnergia
from indicador05.models import Uso
from indicador07.models import Actividad
from indicador08.models import Animales
from indicador09.models import Cultivos
from indicador10.models import ManejoAgro
from indicador11.models import Variedades
from indicador13.models import Rubros
from indicador14.models import TipoTrabajo
from indicador15.models import Equipos, NombreHerramienta, NombreTransporte
from indicador16.models import AhorroPregunta
from indicador18.models import Alimentos
from indicador19.models import Fenomeno
from indicador20.models import PreguntaRiesgo


def globales(request):
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

    return {'tiposexo':tiposexo, 'PEnergia':PEnergia, 'usotierra':usotierra,
            'reforestacion':reforestacion, 'animales':animales, 'cultivos':cultivos,
            'manejo':manejo, 'semilla':semilla, 'rubro':rubro, 
            'otrosingresos':otrosingresos, 'equipo':equipo, 'herramienta':herramienta,
            'transporte':transporte, 'ahorro':ahorro, 'seguridad':seguridad,
            'fenomeno':fenomeno, 'riesgos':riesgos}