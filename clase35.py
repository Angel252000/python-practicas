from Consulta import Consulta
from paciente import Paciente


pacientes = []
Consultas = []

def crear_nueva_consulta():
    nombre_paciente = input("Ingrese el nombre del paciente: ")
    for paciente in pacientes:
        if paciente.nombre == nombre_paciente:
            peso = float(input("Ingrese el peso del paciente (kg): "))
            sintomatologia = input("Ingrese la sintomatología: ")
            notas_evaluacion_fisica = input("Ingrese las notas de evaluación física: ")
            diagnostico = input("Ingrese el diagnóstico: ")
            requiere_control = input("¿Requiere control? (S/N): ")
            examenes = input("Ingrese los exámenes necesarios: ")
            prescripciones = input("Ingrese las prescripciones: ")
            fecha_consulta = input("Ingrese la fecha de consulta (dd-mm-yyyy): ")
            Consulta = Consulta(paciente, peso, sintomatologia, notas_evaluacion_fisica, diagnostico, requiere_control, examenes, prescripciones, fecha_consulta)
            print("Consulta creada exitosamente.")
            return
    print("Paciente no encontrado. Intente de nuevo.")

def registrar_nuevo_paciente():
    tipo = input("Ingrese el tipo de animal: ")
    raza = input("Ingrese la raza del animal: ")
    color = input("Ingrese el color del animal: ")
    edad = input("Ingrese la edad del animal: ")
    nombre = input("Ingrese el nombre del paciente: ")
    nombre_representante = input("Ingrese el nombre del representante: ")
    telefono = input("Ingrese el teléfono del representante: ")
    correo = input("Ingrese el correo del representante: ")
    direccion = input("Ingrese la dirección del representante: ")
    paciente = Paciente(tipo, raza, color, edad, nombre, nombre_representante, telefono, correo, direccion)
    pacientes.append(paciente)
    print("Paciente registrado exitosamente.")

def buscar_paciente():
    nombre_paciente = input("Ingrese el nombre del paciente: ")
    for paciente in pacientes:
        if paciente.nombre == nombre_paciente:
            print("Información del paciente:")
            print(f"Tipo: {paciente.tipo}")
            print(f"Raza: {paciente.raza}")
            print(f"Color: {paciente.color}")
            print(f"Edad: {paciente.edad}")
            print(f"Nombre: {paciente.nombre}")
            print(f"Nombre del representante: {paciente.nombre_representante}")
            print(f"Teléfono: {paciente.telefono}")
            print(f"Correo: {paciente.correo}")
            print(f"Dirección: {paciente.direccion}")
            print("Consultas:")
            for i, Consulta in enumerate(paciente.consultas):
                print(f"{i+1}. {Consulta.fecha_consulta}")
            return
    print("Paciente no encontrado.")

def main():
    while True:
        print("Menú principal:")
        print("1. Crear nueva consulta")
        print("2. Registrar nuevo paciente")
        print("3. Buscar paciente")
        opcion = input("Ingrese una opción: ")
        if opcion =="1":
            crear_nueva_consulta()
        elif opcion == "2":
            registrar_nuevo_paciente()
        elif opcion == "3":
            buscar_paciente()
        elif opcion == "--":
            print("Regresando al menú principal.")
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()