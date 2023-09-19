from zooAnimales import mamifero
from zooAnimales import ave
from zooAnimales import pez
from zooAnimales import reptil
from zooAnimales import anfibio

class Animal():

    _totalAnimales = 0

    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None, zona = None):

        if zona == None:
            zona = []

        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona 
        Animal._totalAnimalestotalAnimales += 1

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad
    
    def setEdad(self, nombre):
        self._edad = nombre

    def getHabitat(self):
        return self._habitat
    
    def setHabitat(self, nombre):
        self._habitat = nombre
    
    def getGenero(self):
        return self._genero
    
    def setGenero(self, nombre):
        self._genero = nombre

    def getZona(self):
        return self._zona
    
    def setZona(self, nombre):
        self._zona = nombre

    @classmethod
    def getTotalAnimales(cls):
        return Animal._totalAnimales
    
    @classmethod
    def setTotalAnimales(cls, total):
        Animal._totalAnimales = total
    
    @classmethod
    def totalAnimales(cls):
        Animal.getTotalAnimales()

    @classmethod
    def totalPorTipo(cls):
        
        totalmamiferos = len(mamifero.getListado())
        totalaves = len(ave.getListado())
        totalreptiles = len(reptil.getListado())
        totalpeces = len(pez.getListado())
        totalanfibios = len(anfibio.getListado())

        return (f"Mamiferos: {totalmamiferos}\nAves:  {totalaves}\nReptiles:  {totalreptiles}\nPeces: {totalpeces}\nAnfibios: {totalanfibios}")