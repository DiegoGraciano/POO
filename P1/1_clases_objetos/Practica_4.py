import os
os.system("cls")

class Alumnos:

    def __init__(self,nombre,edad,matricula):
        self.__nombre = nombre
        self.__edad = edad
        self.__matricula = matricula
        
    def inscribirse(self):
        pass

    def estudiar(self):
        pass


alumno1=Alumnos("Diego",19,151468)
alumno2=Alumnos("Chuy",20,151448)


class Cursos:

    def __init__(self,nombre,codigo,creditos):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__creditos = creditos
         
    def inscribirse(self):
        pass

    def estudiar(self):
        pass


curso1=Cursos("Ingles","A15D",5)
curso2=Cursos("Mate","B15D",10)

class Profesor:

    def __init__(self,nombre,experiencia,num_profesor):
        self.__nombre = nombre
        self.__experiencia = experiencia
        self.__num_profesor = num_profesor
        
    def inscribirse(self):
        pass

    def estudiar(self):
        pass


profesor1=Profesor("Luis","15 años",14)
profesor2=Profesor("Raul","25 años",15)


    

            
        