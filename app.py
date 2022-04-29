class Alumno:

    def __init__(self):
        self.nombre = 'Nestor Antonio'
        self.nota = 5.9
    
    def imprimir(self):
        print("Nombre: ", self.nombre)
        if(self.nota >= 6):
            print("Aprobado con: ", self.nota)
        else:
            print("No ha aprobado con:",self.nota)

alumno = Alumno()
alumno.imprimir()