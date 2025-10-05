import os 
os.system("cls")

class Clase:
    atributo_publico="Soy un atributo publico"
    _atributo_protegido="Soy un atrubuto protegido"
    __atributo_privado="Soy un atributo priavado"

    def getAtributoPrivado(self):
        return self.__atributo_privado
    
    def setAtributoPrivado(self,atributo_privado)
        self.__atributo_privado=atributo_privado

    @property
    def color(self):
        return self.color 
    
    @color.setter
    def color(self,color):
        self.__color=color







