from gestion import zona

class Zoologico():

    def __init__(self, nombre = None, ubicacion = None, zonas = None):

        if zonas == None:
            zonas = []

        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = zonas

    def cantidadTotalAnimales(self):

        cont = 0

        for i in self._zonas:
           
            K = i.getAnimales()
            cont += len(K)

        return cont
    
    def agragarzonas(self, zona):

        self._zonas.append(zona)