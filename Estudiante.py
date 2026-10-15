from Persona import Persona 

class Estudiante(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, 'Estudiante')
        self.materias = []

    def matricular_materia(self, materia):
        self.materias.append(materia)
        materia.matricular_alumno(self)
        print(f"El alumno {self.nombre} se ha matriculado en la materia {materia.nombre}.")

    def ver_materias(self):
        print(f'Materias del alumno {self.nombre}:')
        for materia in self.materias:
            promedio = materia.promedio if materia.promedio is not None else "N/A"
            print(f"• {materia.nombre}, profesor: {materia.profesor}, promedio: {promedio}")

    def agregar_calificacion_materia(self, nombre_materia, calificacion):
        for materia in self.materias:
            if materia.nombre == nombre_materia:
                materia.asignar_nota(calificacion, self.nombre)
                return
        print(f"No estás matriculado en la materia {nombre_materia}. No se puede asignar la calificación.")
