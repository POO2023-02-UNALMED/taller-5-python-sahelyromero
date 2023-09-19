class Zona:
    
    def __init__(self, nombre = None, ubicacion = None, animales = None):
        
        if animales == None:
            animales = []

        self.nombre = nombre
        self.ubicacion = ubicacion
        self.animales = animales
