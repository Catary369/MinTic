# -*- coding: utf-8 -*-
"""torneo

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VYFhGGMbLv339YEdEXSlg1QQAV6rYUDu
"""

# Funcion 1 ---------------------------------------------------------------------------------

def equipos(lista_equipo):
  interesantes = []
  interesantes.append(lista_equipo[0])
  for equipo in lista_equipo:
    if equipo not in interesantes:
      interesantes.append(equipo)
  return interesantes

#print(equipos(["Newpi", "San Francis", "Naughty Boys", "Newpi", "Newpi", "Naughty Boys", "Newpi", "San Francis"]))

# Funcion 2 ---------------------------------------------------------------------------------

def miequipo(posiciones_j, equipos_j, nombre_e):
  posiciones = []
  for posicion in posiciones_j:
    for equipo in range(len(equipos_j)):
      e_ = equipos_j[equipo]
      if nombre_e == e_ and equipo == posicion:
        posiciones.append(posicion)
  return posiciones

#print(miequipo([1,3,5,6], ["Newpi", "San Francis", "Naughty Boys", "Newpi", "Newpi", "Naughty Boys", "Newpi", "San Francis"], "Newpi"))

# Funcion 3 ---------------------------------------------------------------------------------

def faltantes(posiciones_local, posiciones_solicitadas):
  posiciones_f1 = []
  faltan1 = 0
  for posicion in posiciones_local:
    if posicion not in posiciones_solicitadas:
      posiciones_f1.append(posicion)
      faltan1 += 1
  return posiciones_f1

#print(faltantes([3,5,7,10,15,16],[3,5,10,13]))

# Funcion 4 ---------------------------------------------------------------------------------

def diferencia(posiciones_local, posiciones_solicitadas):
  posiciones_f2 = []
  faltan2 = 0
  posiciones_f3 = faltantes(posiciones_local, posiciones_solicitadas)
  faltan3 = len(posiciones_f3)

  for posicion in posiciones_solicitadas:
    if posicion not in posiciones_local:
      posiciones_f2.append(posicion)
      faltan2 += 1
    
  if faltan2 < faltan3:
    return faltan2
  else:
    return faltan3


print(diferencia([3,5,7,10,15,16],[3,5,10,13]))