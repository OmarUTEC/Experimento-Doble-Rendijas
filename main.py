import math
from function import *

'''PARAMETROS DE ENTRADA'''

'''longitud_de_onda'''

Lambda = 2*10**(-2)

'''distancia_pantalla'''

D = 13

'''angulo'''

ß = 4*math.pi/180

'''numero de puntos'''

M = 1050

'''Lista de las posiciones de cada rendija'''

List_Rend = [4,-7]

var = mi_funtion.PatronIntensidad(Lambda, D, ß, M, List_Rend)

mi_funtion.grafico_del_patron(var)