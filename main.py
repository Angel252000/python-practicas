from Gestor_ingresos_personales import GestorIngresosPersonales

def main():
    gestor = GestorIngresosPersonales()

    while True:
        print("\n--- Sistema de Ingresos Personales ---")
        print("1. Añadir Ingreso")
        print("2. Añadir Categoría")
        print("3. Añadir Presupuesto")
        print("4. Generar Reporte")
        print("5. Ver Ingresos")
        print("6. Ver Categorías")
        print("7. Ver Presupuestos")
        print("8. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            try:
                cantidad = float(input("Cantidad: "))
                fecha = input("Fecha (YYYY-MM-DD): ")
                descripcion = input("Descripción: ")
                categoria = input("Categoría: ")
                gestor.añadir_ingreso(cantidad, fecha, descripcion, categoria)
            except ValueError:
                print("Error: La cantidad debe ser un número.")

        elif opcion == '2':
            nombre = input("Nombre de la Categoría: ")
            gestor.añadir_categoria(nombre)

        elif opcion == '3':
            try:
                cantidad = float(input("Cantidad del Presupuesto: "))
                periodo = input("Período del Presupuesto (mensual/anual): ")
                gestor.añadir_presupuesto(cantidad, periodo)
            except ValueError:
                print("Error: La cantidad debe ser un número.")

        elif opcion == '4':
            gestor.generar_reporte()

        elif opcion == '5':
            gestor.ver_ingresos()

        elif opcion == '6':
            gestor.ver_categorias()

        elif opcion == '7':
            gestor.ver_presupuestos()

        elif opcion == '8':
            break

        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()
