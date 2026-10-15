registro_estudiantes = {}

def añadir_estudiante(nombre):
    registro_estudiantes[nombre] = []

def añadir_calificación(nombre, calificación):
    registro_estudiantes[nombre].append(calificación)

def imprimir_informe():
    for estudiante, calificaciones in registro_estudiantes.lista():
        print(f"{estudiante}: {calificaciones}")

# Ejemplo de uso
añadir_estudiante("Juan")
añadir_calificación("Juan", 85)
añadir_calificación("Juan", 90)
imprimir_informe()
