from animal import Animal

class Ave(Animal):

    _listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None, zona = None, colorPlumas = None):

        super().__init__(self, nombre, edad, habitat, genero, zona)

        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

    def getColorPlumas(self):
        return self._colorPlumas
    
    def setColorPlumas(self, color):
        self._colorPlumas = color

    @classmethod
    def getListado(cls):
        return Ave._listado
    
    @classmethod
    def setListado(cls, listado):
        Ave._listado = listado

    @classmethod
    def getHalcones(cls):
        return Ave.halcones
    
    @classmethod
    def setHalcones(cls, listado):
        Ave.halcones = listado

    @classmethod
    def getAguilas(cls, listado):
        Ave.aguilas = listado

    @classmethod
    def setRanas(cls, listado):
        Ave.aguilas = listado