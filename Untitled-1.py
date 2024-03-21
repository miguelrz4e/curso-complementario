class Persona:
    total_personas = 0
    
    def _init_(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        Persona.total_personas += 1
    
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")


class Estudiante(Persona):
    total_estudiantes = 0
    
    def _init_(self, nombre, edad, carrera):
        super()._init_(nombre, edad)
        self.carrera = carrera
        Estudiante.total_estudiantes += 1
    
    def info_estudiante(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}")


class Empleado:
    def trabajar(self, horas):
        print(f"Trabajé {horas} horas.")


class EstudianteEmpleado(Estudiante, Empleado):
    def _init_(self, nombre, edad, carrera, salario):
        super()._init_(nombre, edad, carrera)
        self.salario = salario
    
    def info_empleado(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Carrera: {self.carrera}, Salario: ${self.salario}")


# Ejemplo de uso
persona1 = Persona("Edwar", 20)
persona1.saludar()

estudiante1 = Estudiante("Miguel", 20, "zootecnia")
estudiante1.saludar()
estudiante1.info_estudiante()

empleado1 = Empleado()
empleado1.trabajar(8)

estudiante_empleado1 = EstudianteEmpleado("Edwar", 20, "Ingenieria", 1000)
estudiante_empleado1.saludar()
estudiante_empleado1.info_estudiante()
estudiante_empleado1.trabajar(6)
estudiante_empleado1.info_empleado()