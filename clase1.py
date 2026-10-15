def main():
    nombre = input("Ingrese el nombre del estudiante: ")
    calificaciones = pedir_calificaciones()
    promedio = calcular_promedio(calificaciones)

    print("\nNombre del estudiante:", nombre)
    print("Promedio de calificaciones:", promedio)

def pedir_calificaciones():
    print("Ingresa tus últimas 10 calificaciones: ")
    calificacion1 = float(input("Calificación 1: "))
    calificacion2 = float(input("Calificación 2: "))
    calificacion3 = float(input("Calificación 3: "))
    calificacion4 = float(input("Calificación 4: "))
    calificacion5 = float(input("Calificación 5: "))
    calificacion6 = float(input("Calificación 6: "))
    calificacion7 = float(input("Calificación 7: "))
    calificacion8 = float(input("Calificación 8: "))
    calificacion9 = float(input("Calificación 9: "))
    calificacion10 = float(input("Calificación 10: "))
    calificaciones = [calificacion1, calificacion2, calificacion3, calificacion4, calificacion5,
                      calificacion6, calificacion7, calificacion8, calificacion9, calificacion10]
    return calificaciones

def calcular_promedio(calificaciones):
    total = sum(calificaciones)
    promedio = total / len(calificaciones)
    return promedio

main()
