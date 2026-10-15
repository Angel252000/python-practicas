class Computadora:
    def __init__(self, marca, modelo, procesador, ram, almacenamiento, sistema_operativo, precio, cantidad_disponible, pantalla, tarjeta_grafica, tipo_conexion, peso):
        self.marca = marca
        self.modelo = modelo
        self.procesador = procesador
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.sistema_operativo = sistema_operativo
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible
        self.pantalla = pantalla
        self.tarjeta_grafica = tarjeta_grafica
        self.tipo_conexion = tipo_conexion
        self.peso = peso

    def mostrar_informacion(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Procesador:", self.procesador)
        print("RAM:", self.ram)
        print("Almacenamiento:", self.almacenamiento)
        print("Sistema Operativo:", self.sistema_operativo)
        print("Precio:", self.precio)
        print("Cantidad Disponible:", self.cantidad_disponible)
        print("Pantalla:", self.pantalla)
        print("Tarjeta Gráfica:", self.tarjeta_grafica)
        print("Tipo de Conexión:", self.tipo_conexion)
        print("Peso:", self.peso)

    def actualizar_precio(self, nuevo_precio):
        "Actualiza el precio de la computadora."
        self.precio = nuevo_precio

    def cambiar_ram(self, nueva_ram):
        "Cambia la cantidad de RAM de la computadora."
        self.ram = nueva_ram

    def actualizar_almacenamiento(self, nuevo_almacenamiento):
        "Actualiza la capacidad de almacenamiento de la computadora."
        self.almacenamiento = nuevo_almacenamiento

    def actualizar_marca(self, nueva_marca):
        "Actualiza la marca de la computadora."
        self.marca = nueva_marca

    def actualizar_peso(self, nuevo_peso):
        "Actualiza el peso de la computadora."
        self.peso = nuevo_peso

    def definir_tarjeta_grafica(self, tarjeta):
        "Define la tarjeta gráfica de la computadora."
        self.tarjeta_grafica = tarjeta


computadora = Computadora("HP","Pavilion","Intel Core i5","8 GB","512 GB SSD","Windows 10",800.00,30,"15.6 pulgadas","NVIDIA GeForce MX250","Wi-Fi, Bluetooth","2.5 kg")

print("Información de la computadora:")
computadora.mostrar_informacion()

computadora.actualizar_precio(850.00)
computadora.cambiar_ram("16 GB")
computadora.actualizar_almacenamiento("1 TB SSD")
computadora.actualizar_marca("Dell")
computadora.actualizar_peso("3.0 kg")
computadora.definir_tarjeta_grafica("NVIDIA GTX 1650")

print("\nInformación actualizada de la computadora:")
computadora.mostrar_informacion()


