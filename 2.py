class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
        def presentarse(self):
            print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")
            
class estudiante(persona):
        def __init__(self, nombre, edad, curso):
            super().__init__(nombre, edad)
            self.curso = curso
            
        def mostrar_curso(self):
            print(f"Estoy estudiando {self.curso}.")
            
    

persona1 = persona("Ana", 30)
estudiante1 = estudiante("Luis", 20, "Python Avanzado")


persona1.presentarse()
estudiante1.presentarse()
print(estudiante1.mostrar_curso())
        
        