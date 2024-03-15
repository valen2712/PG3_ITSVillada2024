class Persona:
     def iniciar(self,name):
        self.nombre=name
     def imprimir(self):
        print("Nombre",self.nombre)


persona1=Persona()
persona1.iniciar("Santiago")
persona1.imprimir()

persona2=Persona()
persona2.iniciar("Mateo")
persona2.imprimir()