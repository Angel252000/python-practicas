class Zapatos:
    def __init__(self, marca, modelo, talla, color, material_exterior, material_interior, tipo_cierre, precio, cantidad_de_zapatos, estilo_suela, estilo_punta, estilo_accesorio):
        self.marca = marca
        self.modelo = modelo
        self.talla = talla
        self.color = color
        self.material_exterior = material_exterior
        self.material_interior = material_interior
        self.tipo_cierre = tipo_cierre
        self.precio = precio
        self.cantidad_de_zapatos = cantidad_de_zapatos
        self.estilo_suela = estilo_suela
        self.estilo_punta = estilo_punta
        self.estilo_accesorio = estilo_accesorio

    def mostrar_informacion(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Talla:", self.talla)
        print("Color:", self.color)
        print("Material Exterior:", self.material_exterior)
        print("Material Interior:", self.material_interior)
        print("Tipo de Cierre:", self.tipo_cierre)
        print("Precio:", self.precio)
        print("Cantidad de Zapatos:", self.cantidad_de_zapatos)
        print("Estilo de Suela:", self.estilo_suela)
        print("Estilo de Punta:", self.estilo_punta)
        print("Estilo de Accesorio:", self.estilo_accesorio)

    def actualizar_precio(self, nuevo_precio):
        "Actualiza el precio de los zapatos."
        self.precio = nuevo_precio

    def cambiar_color(self, nuevo_color):
        "Cambia el color de los zapatos."
        self.color = nuevo_color

    def cambiar_talla(self, nueva_talla):
        "Cambia la talla de los zapatos."
        self.talla = nueva_talla

    def actualizar_material_exterior(self, nuevo_material_exterior):
        "Actualiza el material exterior de los zapatos."
        self.material_exterior = nuevo_material_exterior

    def actualizar_material_interior(self, nuevo_material_interior):
        "Actualiza el material interior de los zapatos."
        self.material_interior = nuevo_material_interior

    def actualizar_marca(self, nueva_marca):
        "Actualiza la marca de los zapatos."
        self.marca = nueva_marca

zapatos = Zapatos("Nike ","nike cortez"," 10","Negro","Cuero","Textil","Cordones",150.00,50,"Suela de Goma","Redonda","Logotipo de Nike")

print("Información de zapatos para niggas:")
zapatos.mostrar_informacion()

zapatos.actualizar_precio(180.00)
zapatos.cambiar_color("Blanco")
zapatos.cambiar_talla(" 11")
zapatos.actualizar_material_exterior("Sintético")
zapatos.actualizar_material_interior("Cuero")
zapatos.actualizar_marca("Adidas")

print("\nInformación de zapatos para blancos:")
zapatos.mostrar_informacion()
