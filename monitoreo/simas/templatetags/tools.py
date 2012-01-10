from django import template
import locale
register = template.Library()

@register.filter
def restar(value, arg):    
    return int(value)-int(arg)

@register.filter
def total_dict(value):    
    return sum(value.values())

@register.filter
def total_per_key(value, arg):
    '''value es el dict y arg es el key del que se quiere obtener el total o suma'''   
    return sum([v[arg] for v in value.values()])

@register.filter
def total_general(tabla):   
    '''donde tabla es un dicc donde estan todos los valores'''
    return sum([sum(value.values()) for value in tabla.values()]) 

@register.filter
def frecuencia(cantidad, tabla):   
    '''donde cantidad es la cantidad y tabla es todos los valores del dicc'''
    total = total_general(tabla)
    return calcular_frecuencia(cantidad, total)

@register.filter
def get_value(dicc, key):   
    '''donde dicc es el diccionario con valores y key la llave a obtener'''
    return dicc[key]

@register.filter
def get_frec(value, tabla):
    '''value valor a calcular frecuencia sobre total de la tabla'''
    return calcular_frecuencia(value, sum(tabla.values()))

@register.filter
def calcular_frecuencia(cantidad, total):
    if total == None or cantidad == None or total == 0:
        x = 0
    else:
        x = (cantidad * 100) / float(total)
    return round(x, 1)

@register.filter()
def currency(value):    
    return '{:20,.2f}'.format(value)

@register.filter()
def exclude(list, key):
    return [foo for foo in list if foo != key]

@register.filter
def truncate_init(value, arg):
    return value[int(arg):]

@register.filter
def frec_acumul(lista, index):    
    return sum(lista[index:])

@register.filter
def dolarizar(cantidad, tasa):
    return int(cantidad/tasa) 

