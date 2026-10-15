saldo = 0

def depositar(cantidad):
    global saldo
    if cantidad > 0:
        saldo += cantidad
        print("Depósito exitoso. Nuevo saldo:", saldo)
    else:
        print("Error: La cantidad a depositar debe ser positiva.")

def retirar(cantidad):
    global saldo
    if cantidad > 0:
        if saldo >= cantidad:
            saldo -= cantidad
            print("Retiro exitoso. Nuevo saldo:", saldo)
        else:
            print("Error: Fondos insuficientes.")
    else:
        print("Error: La cantidad a retirar debe ser positiva.")

def consultar_saldo():
    print("Saldo actual:", saldo)

while True:
    print("\n¿Qué operación desea realizar?")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Consultar saldo")
    print("4. Salir")
    opcion = input("Ingrese el número de la operación: ")

    if opcion == "1":
        cantidad = float(input("Ingrese la cantidad a depositar: "))
        depositar(cantidad)
    elif opcion == "2":
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        retirar(cantidad)
    elif opcion == "3":
        consultar_saldo()
    elif opcion == "4":
        print("Gracias por utilizar nuestro servicio. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese un número válido.")
