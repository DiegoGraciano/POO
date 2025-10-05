#Ejercicio practico
import os
#crear clases
class coches:
    #Metodo Contructor "__init__"
    def __init__(self,color,marca,velocidad):
        self.color=color
        self.marca=marca
        self.velocidad=velocidad

    def acelerar(self,incremento):
        self.velocidad=self.velocidad+incremento
        return self.velocidad
    
    def frenar(self,decremento):
        self.velocidad=self.velocidad-decremento
        return self.velocidad
    
    def tocar_claxon(self):
        return "PIIIII"
    
#Instanciar objetos de la clase coches

coche1=coches("Blanco","Toyota",200)
coche2=coches("Amarillo","Ford",180)
coche3=coches("Negro","Honda",150)

print(f"Los valores del objeto 1 {coche1.color},{coche1.marca},{coche1.velocidad}")
print(f"La velocidad del coche 1 es {coche1.velocidad} y cambio a {coche1.acelerar(50)}")

print(f"Los valores del objeto 2 {coche2.color},{coche2.marca},{coche2.velocidad}")
print(f"La velocidad del coche 2 es {coche1.velocidad} y cambio a {coche1.frenar(100)}")

print(f"Los valores del objeto 1 {coche3.color},{coche3.marca},{coche3.velocidad}")
