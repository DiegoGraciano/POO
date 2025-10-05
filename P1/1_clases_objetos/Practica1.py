#Elaborar un programa que calcule el area de un rectangulo
#Implmentar el paradigma estructurado
#Implementar el paradigma OO

#Estructurado 

def area_rectangulo(base,altura):
    return base * altura

print(area_rectangulo(5,3))

#Orientada a Objetos

class Rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
rect = Rectangulo(5,3)
print(rect.area())