class Banco:
    def __init__(self):
        self.cuentas = []
        self.transacciones = []
        self.next_id = 1

    def crear_cuenta(self, denominacion):
        cuenta = Cuenta(self.next_id, denominacion)
        self.cuentas.append(cuenta)
        self.next_id += 1
        print(f"Cuenta creada exitosamente: {cuenta}")

    def obtener_cuentas(self):
        return self.cuentas

    def buscar_cuenta(self, cuenta_id):
        for cuenta in self.cuentas:
            if cuenta.id == cuenta_id:
                return cuenta
        return None

    def registrar_transaccion(self, tipo, monto, cuenta_id):
        transaccion = Transaccion(tipo, monto, cuenta_id)
        self.transacciones.append(transaccion)

    def ver_libro_diario(self):
        if not self.transacciones:
            print("No hay transacciones registradas.")
        else:
            for transaccion in self.transacciones:
                print(transaccion)

    def menu_principal(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Crear cuenta")
            print("2. Depositar")
            print("3. Retirar")
            print("4. Consultar saldo")
            print("5. Ver libro diario")
            print("6. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.menu_crear_cuenta()
            elif opcion == "2":
                self.menu_depositar()
            elif opcion == "3":
                self.menu_retirar()
            elif opcion == "4":
                self.menu_consultar_saldo()
            elif opcion == "5":
                self.ver_libro_diario()
            elif opcion == "6":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida")

    def menu_crear_cuenta(self):
        print("\n--- Crear Cuenta ---")
        denominacion = input("Ingrese la denominación de la cuenta (Colones/Dolares): ")
        if denominacion in ["Colones", "Dolares"]:
            self.crear_cuenta(denominacion)
        else:
            print("Denominación inválida. Intente nuevamente.")

    def menu_depositar(self):
        print("\n--- Depositar ---")
        if not self.cuentas:
            print("No hay cuentas creadas. Cree una cuenta primero.")
            return
        self.listar_cuentas()
        cuenta_id = int(input("Ingrese el ID de la cuenta donde desea depositar: "))
        cuenta = self.buscar_cuenta(cuenta_id)
        if cuenta:
            monto = float(input("Ingrese el monto a depositar: "))
            if cuenta.depositar(monto):
                self.registrar_transaccion('deposito', monto, cuenta_id)
                print("Depósito exitoso.")
            else:
                print("Monto inválido.")
        else:
            print("Cuenta no encontrada.")

    def menu_retirar(self):
        print("\n--- Retirar ---")
        if not self.cuentas:
            print("No hay cuentas creadas. Cree una cuenta primero.")
            return
        self.listar_cuentas()
        cuenta_id = int(input("Ingrese el ID de la cuenta donde desea retirar: "))
        cuenta = self.buscar_cuenta(cuenta_id)
        if cuenta:
            monto = float(input("Ingrese el monto a retirar: "))
            if cuenta.retirar(monto):
                self.registrar_transaccion('retiro', monto, cuenta_id)
                print("Retiro exitoso.")
            else:
                print("Saldo insuficiente.")
        else:
            print("Cuenta no encontrada.")

    def menu_consultar_saldo(self):
        print("\n--- Consultar Saldo ---")
        if not self.cuentas:
            print("No hay cuentas creadas. Cree una cuenta primero.")
            return
        self.listar_cuentas()
        cuenta_id = int(input("Ingrese el ID de la cuenta donde desea consultar el saldo: "))
        cuenta = self.buscar_cuenta(cuenta_id)
        if cuenta:
            print(f"Saldo de la cuenta {cuenta_id}: {cuenta.balance}")
        else:
            print("Cuenta no encontrada.")

    def listar_cuentas(self):
        for cuenta in self.cuentas:
            print(cuenta)


class Cuenta:
    def __init__(self, identificador, denominacion):
        self.id = identificador
        self.denominacion = denominacion
        self.balance = 0

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto
            return True
        return False

    def retirar(self, monto):
        if monto > 0 and self.balance >= monto:
            self.balance -= monto
            return True
        return False

    def __str__(self):
        return f"Cuenta ID: {self.id}, Denominación: {self.denominacion}, Balance: {self.balance}"


class Transaccion:
    def __init__(self, tipo, monto, cuenta_id):
        self.tipo = tipo
        self.monto = monto
        self.cuenta_id = cuenta_id

    def __str__(self):
        return f"{self.tipo.capitalize()} de {self.monto} en cuenta ID {self.cuenta_id}"


if __name__ == "__main__":
    banco = Banco()
    banco.menu_principal()
