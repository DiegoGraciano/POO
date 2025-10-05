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
        return self.potencia
    
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
class Camiones(Coches):
   def __init__(self, marca, color, modelo, velocidad, potencia, plazas,eje,capacidadCarga):
      super().__init__(marca, color, modelo, velocidad, potencia, plazas)
      self.__eje=eje
      self.__capacidadCarga=capacidadCarga
    

   def cargar(self,tipo_carga):
      self.tipo_carga=tipo_carga

   def acelerar(self):
       return "Estas Acelerando el Camion"
   
   def frenar(self):
      return "Estas Frenando el Camion"
    
   @property
   def eje(self):
      self.__eje

   @eje.setter
   def eje(self,eje):
      self.__eje=eje

   @property
   def capacidadCarga(self):
      self.__capacidadCarga

   @capacidadCarga.setter
   def capacidadCarga(self,capacidadCarga):
      self.__capacidadCarga=capacidadCarga

    

class Camionetas(Coches):
   def __init__(self, marca, color, modelo, velocidad, potencia, plazas,cerrada,traccion):
      super().__init__(marca, color, modelo, velocidad, potencia, plazas)
      self.__traccion=traccion
      self.__cerrada=cerrada
    

   def transportar(self,num_pasajeros):
      self.__num_pasajeros=num_pasajeros

   def acelerar(self):
       return "Estas Acelerando el Camion"
   
   def frenar(self):
      return "Estas Frenando el Camion"
    
   @property
   def traccion(self):
      self.__traccion

   @traccion.setter
   def traccion(self,traccion):
      self.__traccion=traccion

   @property
   def cerrada(self):
      self.__cerrada

   @cerrada.setter
   def cerrada(self,cerrada):
      self.__cerrada=cerrada
   

      
