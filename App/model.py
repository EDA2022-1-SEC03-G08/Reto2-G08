"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():

    catalog = {"albums": None,
               "artists": None,
               "tracks": None}
    # No se neceistan listas encadenadas pues la información solo se va a
    # consultar pero no a alterar. Por otro lado siempre se añade
    # un album, artista o canción
    # al final de la lista
    # cosa que no tiene repercusiones de tiempo en un arreglo

    #TODO: Cambiar el 1000 por el tamaño de datos reales. Para evitar rehash.
    catalog["albums"] = mp.newMap(1000,
                                   maptype='CHAINING',
                                   loadfactor=4,
                                   comparefunction=compareAlbums)

    catalog["artists"] = mp.newMap(1000,
                                   maptype='CHAINING',
                                   loadfactor=4,
                                   comparefunction=compareArtists)

    catalog["tracks"] = mp.newMap(1000,
                                   maptype='CHAINING',
                                   loadfactor=4,
                                   comparefunction=compareTracks)

    return catalog

# Funciones para agregar informacion al catalogo

def addAlbum(catalog, album):
    mp.put(catalog['albums'], album['id'], album)


def addArtist(catalog, artistdic):
    mp.put(catalog['artists'], artistdic['id'], artistdic)


def addTrack(catalog, track):
    mp.put(catalog['tracks'], track['id'], track)


# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def compareAlbums(album1, album2):
    """
    Compara dos ids de dos albumes
    """
    identry = me.getKey(album2)
    if (album1 == identry):
        return 0
    elif album1 > identry:
        return 1
    else:
        return -1


def compareArtists(artist1, artist2):
    """
    Compara dos ids de dos artistas
    """
    identry = me.getKey(artist2)
    if (artist1 == identry):
        return 0
    elif artist1 > identry:
        return 1
    else:
        return -1


def compareTracks(track1, track2):
    """
    Compara dos ids de dos tracks
    """
    identry = me.getKey(track2)
    if (track1 == identry):
        return 0
    elif track1 > identry:
        return 1
    else:
        return -1



# Funciones de ordenamiento

# FUnciones de inidcadores de tamaño

def albumSize(catalog):
    return mp.size(catalog['albums'])


def artistSize(catalog):
    return mp.size(catalog['artists'])


def trackSize(catalog):
    return mp.size(catalog['tracks'])