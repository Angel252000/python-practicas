class Materia:
    def __init__(self, nombre, aula, creditos, profesor, horario, semestre, facultad, tipo, prerequisitos, estudiantes, duracion, modalidad):
        self.nombre = nombre
        self.aula = aula
        self.creditos = creditos
        self.profesor = profesor
        self.horario = horario
        self.semestre = semestre
        self.facultad = facultad
        self.tipo = tipo
        self.prerequisitos = prerequisitos
        self.estudiantes = estudiantes
        self.duracion = duracion
        self.modalidad = modalidad

    def mostrar_informacion(self):
        print("Nombre del curso:", self.nombre)
        print("Aula:", self.aula)
        print("Créditos:", self.creditos)
        print("Profesor:", self.profesor)
        print("Horario:", self.horario)
        print("Semestre:", self.semestre)
        print("Facultad:", self.facultad)
        print("Tipo de curso:", self.tipo)
        print("Prerrequisitos:", self.prerequisitos)
        print("Número de estudiantes:", self.estudiantes)
        print("Duración:", self.duracion)
        print("Modalidad:", self.modalidad)

    def cambiar_horario(self, nuevo_horario):
        """Cambia el horario del curso."""
        self.horario = nuevo_horario

    def agregar_estudiantes(self, num_estudiantes):
        """Agrega un número de estudiantes al curso."""
        self.estudiantes += num_estudiantes

    def actualizar_profesor(self, nuevo_profesor):
        """Actualiza el nombre del profesor del curso."""
        self.profesor = nuevo_profesor

    def actualizar_prerrequisitos(self, nuevos_prerrequisitos):
        """Actualiza los prerrequisitos del curso."""
        self.prerequisitos = nuevos_prerrequisitos

    def cambiar_modalidad(self, nueva_modalidad):
        """Cambia la modalidad del curso (presencial, online, etc.)."""
        self.modalidad = nueva_modalidad

    def reducir_creditos(self, creditos_a_reducir):
        """Reduce los créditos del curso."""
        self.creditos -= creditos_a_reducir


materia = Materia("Matemáticas","MATA6",4,"Angel Amaya","Lunes a las 6:30","Segundo semestre","Facultad de Ciencias","Obligatoria","Ninguno",30,"16 semanas","Presencial")

print("Antes de los cambios de los cambios de supercell:")
materia.mostrar_informacion()

materia.cambiar_horario("Miércoles a las 10:00")
materia.agregar_estudiantes(5)
materia.actualizar_profesor("María López")
materia.actualizar_prerrequisitos("Matemáticas Básicas")
materia.cambiar_modalidad("Online")
materia.reducir_creditos(1)

print("\nDespués de los cambios de supercell:")
materia.mostrar_informacion()
