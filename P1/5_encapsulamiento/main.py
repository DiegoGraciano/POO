from coches import *

num_coches=int(input("Cuantos coches tienes?: "))

for i in range(0,num_coches):

    print("\n\t..::Datos dek Automovil::..")
    marca=input("Ingrssar marca: ").upper()
    color=input("Ingresar color: ").upper()
    modelo=input("Ingrssar modelo: ").upper()
    velocidad=int(input("Ingresar velocidad: "))
    potencia=int(input("Ingrssar potencia: "))
    plazas=int(input("Ingresar plazas: "))


    coche1=Coches(marca,color,modelo,velocidad,potencia,plazas)

    print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getPotencia()} \n plazas: {coche1.getPlazas()} ")