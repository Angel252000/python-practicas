from Estudiante import Estudiante
from Profesor import Profesor
from Materia import Materia

def main():
    # Se crea una materia
    progra1 = Materia('Programacion 1')
    calculo1 = Materia('Calculo 1')
    
    # Se registra profesor
    profesorProgra = Profesor('Eduardo', 28)
    profesorCalculo = Profesor('Dodanim', 50)
    
    # Asignamos profesor a materia
    progra1.asignar_profesor(profesorProgra)
    calculo1.asignar_profesor(profesorCalculo)

    # Se registran alumnos
    alumno1 = Estudiante('Pedro', 19)
    alumno2 = Estudiante('Maria', 22)
    alumno3 = Estudiante('Juan', 25)

    # Se matriculan alumnos a Programacion 1
    alumno1.matricular_materia(progra1)
    alumno2.matricular_materia(progra1)
    alumno3.matricular_materia(progra1)

    # Se matricula a alumno Pedro a Calculo 1
    alumno1.matricular_materia(calculo1)
    alumno2.matricular_materia(calculo1)

    print('---------')

    alumno1.ver_materias()
    alumno2.ver_materias()
    alumno3.ver_materias()

    print('------')
    progra1.asignar_nota(85, 'Maria')
    calculo1.asignar_nota(74,'juan')
  

if __name__ == '__main__':
    main()
