class Operaciones:
    def __init__(self):
        self.num1 = int(input("Ingrese el primer numero entero"))
        self.num2=int(input("Ingrese el segundo numero entero"))
        self.suma()
        self.resta()
        self.division()
        self.multiplicacion()
    
    def suma (self):
        suma= self.num1 + self.num2
        print(f'El resultado de la suma:', suma)
    
    def resta(self):
        resta = self.num1 - self.num2
        print(f'El resultado de la resta:', resta)

    def division(self):
        div = self.num1 / self.num2
        print(f'El resultado de la division:' , div)

    def multiplicacion (self):
        multi= self.num1*self.num2    
        print(F'El resultado de la multi:', multi)
    
operacion = Operaciones()