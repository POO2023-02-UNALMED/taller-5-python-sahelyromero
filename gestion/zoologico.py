class Zoologico():

    def __init__(self, nombre = None, ubicacion = None):

        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def getUbicacion(self):
        return self._ubicacion
    
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def getZona(self):
        return self._zonas
    
    def setZona(self, zona):
        self._zonas = zona

    def cantidadTotalAnimales(self):

        cont = 0

        for i in self._zonas:
           
            K = i.getAnimales()
            cont += len(K)

        return cont
    
    def agregarZonas(self, zona):

        self._zonas.append(zona)