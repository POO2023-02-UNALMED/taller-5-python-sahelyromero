from gestion.zona import Zona
from zooAnimales.animal import Animal

class Zoologico():

    def __init__(self, nombre = None, ubicacion = None, zonas = None):

        if zonas == None:
            zonas = []

        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = zonas

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def getUbicacion(self):
        return self._ubicacion
    
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def getZonas(self):
        return self._zonas
    
    def setZonas(self, zona):
        self._zonas = zona

    def cantidadTotalAnimales(self):

        cont = 0

        for i in self._zonas:
           
            K = i.getAnimales()
            cont += len(K)

        return cont
    
    def agregarZonas(self, zona):

        self._zonas.append(zona)