from zooAnimales.mamifero import Mamifero
from zooAnimales.ave import Ave
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil
from zooAnimales.anfibio import Anfibio
from gestion import zona
from gestion import zoologico

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
        
        totalmamiferos = len(Mamifero.getListado())
        totalaves = len(Ave.getListado())
        totalreptiles = len(Reptil.getListado())
        totalpeces = len(Pez.getListado())
        totalanfibios = len(Anfibio.getListado())

        return (f"Mamiferos: {totalmamiferos}\nAves: {totalaves}\nReptiles: {totalreptiles}\nPeces: {totalpeces}\nAnfibios: {totalanfibios}")
    
    def __str__(self):

        if len(self._zona) != 0:

            return (f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero} la zona en la que me ubico es {self._zona(0)}, en el {self._zona(0).getZoo()}")
        
        else:

            return (f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}")