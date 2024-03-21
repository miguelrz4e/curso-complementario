#Edwar Arley Fontecha Chiquiza, Miguel Angel Rodriguez Chiquiza
class Persona:
    total_personas = 0
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        Persona.total_personas += 1
    
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

class Estudiante(Persona):
    total_estudiantes = 0
    
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  
        self.carrera = carrera
        Estudiante.total_estudiantes += 1
        
    def imprimir_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}")

class Profesor:
    def __init__(self, nombre, edad, departamento):
        self.nombre = nombre
        self.edad = edad
        self.departamento = departamento
        
    def presentar(self):
        print(f"Soy el profesor {self.nombre}, tengo {self.edad} años y trabajo en el departamento de {self.departamento}.")

class EstudianteProfesor(Estudiante, Profesor):
    def __init__(self, nombre, edad, carrera, departamento):
        Estudiante.__init__(self, nombre, edad, carrera)  
        Profesor.__init__(self, nombre, edad, departamento)  
        
    def info_completa(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}, Departamento: {self.departamento}")

persona1 = Persona("Edwar", 19)
persona1.saludar()

estudiante1 = Estudiante("Miguel", 20, "Ingeniería")
estudiante1.saludar()
estudiante1.imprimir_info()

profesor1 = Profesor("Farley", 35, "ingles")
profesor1.presentar()

estudiante_profesor1 = EstudianteProfesor("luis", 34, "pensamiento sistematico ", "Pensamiento Sistematico")
estudiante_profesor1.saludar()
estudiante_profesor1.imprimir_info()
estudiante_profesor1.presentar()
estudiante_profesor1.info_completa()

print(f"Total de personas registradas: {Persona.total_personas}")
print(f"Total de estudiantes registrados: {Estudiante.total_estudiantes}")
