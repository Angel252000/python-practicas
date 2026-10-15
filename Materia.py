class Materia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.profesor = None
        self.alumnos = []
        self.promedio = None

    def asignar_profesor(self, profesor):
        self.profesor = profesor.nombre
        print(f'Se ha establecido al profesor {self.profesor} para la materia {self.nombre}.')

    def matricular_alumno(self, alumno):
        if len(self.alumnos) < 10:
            self.alumnos.append(alumno)
            print(f"El alumno {alumno.nombre} se ha matriculado en la materia {self.nombre}.")
        else:
            print(f"La matrícula para la materia {self.nombre} está llena. No se puede matricular más estudiantes.")

    def asignar_nota(self, nota, nombre_alumno):
        for alumno in self.alumnos:
            if alumno.nombre == nombre_alumno:
                alumno.nota = nota
                print(f'Se asignó la nota {nota} a {nombre_alumno}.')
                return
        print(f'No se encontró al alumno {nombre_alumno} en la materia {self.nombre}.')

    def obtener_promedio(self):
        notas = [alumno.nota for alumno in self.alumnos if hasattr(alumno, 'nota')]
        if notas:
            self.promedio = sum(notas) / len(notas)
            print(f'El promedio de las notas en la materia {self.nombre} es {self.promedio}.')
        else:
            print(f'No hay notas asignadas en la materia {self.nombre}.')

    def obtener_alumnos(self):
        return [alumno.nombre for alumno in self.alumnos if alumno]
