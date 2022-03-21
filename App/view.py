"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import sys
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

#Inicializacion de catalogo

def newController():
    """
    Se crea una instancia del controlador
    """
    control = controller.newController()
    return control

def newControllerTest(factor, Ctype):
    """
    Se crea una instancia del controlador
    """
    control = controller.newControllerTest(factor, Ctype)
    return control

control = newController()

#Funciones de requerimientos

def loadData():
    """
    Función encargada de entregar la información de carga de los archivos.
    """
    albums, artists, tracks = controller.loadData(control)
    return albums, artists, tracks


def loadDataTest(factor, Ctype):
    controlTest = newControllerTest(factor, Ctype)
    albums, artists, tracks, tiempo, memoria = controller.loadDataTest(controlTest)
    return albums, artists, tracks, tiempo, memoria

    

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- ")
    print("...")
    print("6- Pruebas LAB7")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:

        print("Cargando información de los archivos ....")
    
        # estas tres variables son numero de tipo int

        albums, artists, tracks = loadData()

        # este apartado se encarga de informar al usuario cuantos
        # elementos fueron cargados e incluye la función de imprimir
        # la información de cada lista.

        print("Cargando información de los archivos .... \n")
        print("===================="*2)
        print(f"Cantidad de albumes cargados: {albums} \n")
        print(f"Cantidad de artistas cargados: {artists} \n")
        print(f"Cantidad de canciones cargadas: {tracks}")
        print("===================="*2)

    elif int(inputs[0]) == 2:
        pass

    
    elif int(inputs[0]) == 6:
        print("Cargando información de los archivos ....")
        factor = float(input("Cual es el Factor de Carga?(Ejm. 0.20, 0.90, 2...) \n"))
        Ctype = str(input("CHAINING o PROBING: \n"))
        albums, artists, tracks, tiempo, memoria = loadDataTest(factor, Ctype)

        # este apartado se encarga de informar al usuario cuantos
        # elementos fueron cargados e incluye la función de imprimir
        # la información de cada lista.

        print("Para un map de tipo " + Ctype + " con factor de carga " + str(factor) + ": \n")
        print("===================="*2)
        print(f"Cantidad de datos cargados: {albums+artists+tracks} \n")
        print("===================="*2)
        print(f"Tiempo de carga: {tiempo:.3f} \n")
        print("===================="*2)
        print(f"Consumo de memoria: {memoria:.3f} \n")
        print("===================="*2)
    else:
        sys.exit(0)
sys.exit(0)
