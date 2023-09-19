from animal import Animal

class Mamifero(Animal):

    listado = []
    caballos = 0
    leones = 0

    def __init__(nombre = None, edad = 0, habitat = None, genero = None, zona = None, pelaje = False, patas = 0):
        super().__init__(nombre,edad,habitat,genero,zona)
        
        self.pelaje = pelaje
        self.patas = patas
