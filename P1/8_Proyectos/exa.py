class calculadora:

    def __init__(self,n1,n2):
        self.n1= n1
        self.n2= n2

    def suma(self):
        return self.n1 + self.n2
    
    def resta(self):
        return self.n1 - self.n2
    
    def multiplicacion(self):
        return self.n1 * self.n2

    def division(self):
        return self.n1 / self.n2
    
n1= int(input("N1: "))
n2= int(input("N2: "))

calc= calculadora(n1,n2)

print(f"Suma: {calc.suma()}\nResta: {calc.resta()}\nMultiplicacion: {calc.multiplicacion()}\nDivision: {calc.division()}")


        