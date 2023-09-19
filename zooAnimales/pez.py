from animal import Animal

class Pez(Animal):

    _listado = []
    salmones = 0
    bacalaos = 0
 
    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None, zona = None, colorEscamas = None, cantidadAletas = 0):

        super().__init__(self, nombre, edad, habitat, genero, zona)

        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, color):
        self._colorEscamas = color

    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def setCantidadAletas(self, color):
        self._cantidadAletas = color

    @classmethod
    def getListado(cls):
        return Pez._listado
    
    @classmethod
    def setListado(cls, listado):
        Pez._listado = listado

    @classmethod
    def getSalmones(cls):
        return Pez.salmones
    
    @classmethod
    def setSalmomnes(cls, listado):
        Pez.salmones = listado

    @classmethod
    def getBacalaos(cls, listado):
        Pez.bacalaos = listado

    @classmethod
    def setBacalaos(cls, listado):
        Pez.bacalaos = listado