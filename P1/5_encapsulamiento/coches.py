import os
os.system("cls")

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    #Método constructor para inicalizar los valores de los atributos a la hora de crear o instanciar el objeto de la clase
    
    def __init__(self,marca,color,modelo,velocidad,potencia,plazas):
       self.marca=marca
       self.color=color
       self.modelo=modelo
       self.velocidad=velocidad
       self.potencia=potencia
       self.plazas=plazas
  
  
       
    #Crear los metodos setters y getters, estos metodos son importantes y necesarios en todas las clases para que el programador interactue con los valores de los atributos a traves de estos metodos. . . digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto
    #En teoria se deberia de crear un metodo Getters y Setters por cada atributo que contenga la clase
    #los metodos get siempre regresan valor es decir el valor de la propiedad a traves del return
    #Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion

    #1er forma
    def getMarca(self):
        return self.marca
    def setMarca(self, marca):
       self.marca=marca

    def getColor(self):
        return self.color
    
    def setColor(self, color):
       self.color=color

    def getModelo(self):
        return self.modelo
    
    def setModelo(self, modelo):
       self.modelo=modelo

    def getVelocidad(self):
        return self.velocidad
    
    def setVelocidad(self, velocidad):
       self.velocidad=velocidad

    def getPotencia(self):
        return self.caballaje
    
    def setPotencia(self, potencia):
        self.potencia=potencia

    def getPlazas(self):
        return self.plazas
    
    def setPlazas(self, plazas):
        self.plazas=plazas


    #Metodos o acciones o funciones que hace el objeto
    def acelerar(self):
      return "Estas Acelerando"

    def frenar(self):
      return "Estas Frenando"

#Fin definir clase

#Crear un objetos o instanciar la clase