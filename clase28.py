class Almohada:
    def __init__(self, marca, modelo, tamaño, color, material_exterior, material_interior, relleno, precio, cantidad_de_almohadas, estilo_costura, estilo_cierre, lavable):
        self.marca = marca
        self.modelo = modelo
        self.tamaño = tamaño
        self.color = color
        self.material_exterior = material_exterior
        self.material_interior = material_interior
        self.relleno = relleno
        self.precio = precio
        self.cantidad_de_almohadas = cantidad_de_almohadas
        self.estilo_costura = estilo_costura
        self.estilo_cierre = estilo_cierre
        self.lavable = lavable

    def mostrar_informacion(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Tamaño:", self.tamaño)
        print("Color:", self.color)
        print("Material Exterior:", self.material_exterior)
        print("Material Interior:", self.material_interior)
        print("Relleno:", self.relleno)
        print("Precio:", self.precio)
        print("Cantidad de Almohadas:", self.cantidad_de_almohadas)
        print("Estilo de Costura:", self.estilo_costura)
        print("Estilo de Cierre:", self.estilo_cierre)
        print("Lavable:", self.lavable)

    def actualizar_precio(self, nuevo_precio):
        "Actualiza el precio de la almohada."
        self.precio = nuevo_precio

    def cambiar_color(self, nuevo_color):
        "Cambia el color de la almohada."
        self.color = nuevo_color

    def cambiar_tamaño(self, nuevo_tamaño):
        "Cambia el tamaño de la almohada."
        self.tamaño = nuevo_tamaño

    def actualizar_material_exterior(self, nuevo_material_exterior):
        "Actualiza el material exterior de la almohada."
        self.material_exterior = nuevo_material_exterior

    def actualizar_material_interior(self, nuevo_material_interior):
        "Actualiza el material interior de la almohada."
        self.material_interior = nuevo_material_interior

    def actualizar_marca(self, nueva_marca):
        "Actualiza la marca de la almohada."
        self.marca = nueva_marca


almohada = Almohada("Sognare","Ergonómica","Queen","Blanco","Algodón","Espuma viscoelástica","Fibra de poliéster",50.00,10,"Doble costura","Cremallera","si")

print("Información de la almohada:")
almohada.mostrar_informacion()

almohada.actualizar_precio(60.00)
almohada.cambiar_color("Gris")
almohada.cambiar_tamaño("grande")
almohada.actualizar_material_exterior("Poliéster")
almohada.actualizar_material_interior("pluma")
almohada.actualizar_marca("ositocariñositos")

print("\nInformación actualizada de la almohada:")
almohada.mostrar_informacion()
