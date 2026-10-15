class Camisa:
    def __init__(self, marca, modelo, talla, color, material, tipo_manga, tipo_cuello, precio, cantida_de_camisas, largo_manga, estilo_cierre, estilo_botones):
        self.marca = marca
        self.modelo = modelo
        self.talla = talla
        self.color = color
        self.material = material
        self.tipo_manga = tipo_manga
        self.tipo_cuello = tipo_cuello
        self.precio = precio
        self.cantida_de_camisa = cantida_de_camisas
        self.largo_manga = largo_manga
        self.estilo_cierre = estilo_cierre
        self.estilo_botones = estilo_botones

    def mostrar_informacion(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Talla:", self.talla)
        print("Color:", self.color)
        print("Material:", self.material)
        print("Tipo de Manga:", self.tipo_manga)
        print("Tipo de Cuello:", self.tipo_cuello)
        print("Precio:", self.precio, "USD")
        print("cantida_de_camisas:", self.cantida_de_camisa)
        print("Largo de Manga:", self.largo_manga)
        print("Estilo de Cierre:", self.estilo_cierre)
        print("Estilo de Botones:", self.estilo_botones)

    def actualizar_precio(self, nuevo_precio):
        "Actualiza el precio de la camisa."
        self.precio = nuevo_precio

    def actualizar_largo_manga(self, nuevo_largo_manga):
        "Actualiza el largo de la manga de la camisa."
        self.largo_manga = nuevo_largo_manga


    def cambiar_color(self, nuevo_color):
        "Cambia el color de la camisa."
        self.color = nuevo_color

    def cambiar_talla(self, nueva_talla):
        "Cambia la talla de la camisa."
        self.talla = nueva_talla

    def actualizar_material(self, nuevo_material):
        "Actualiza el material de la camisa."
        self.material = nuevo_material

    def actualizar_marca(self, nueva_marca):
        "Actualiza el material de la camisa."
        self.nueva_marca = nueva_marca


camisa = Camisa("H&M","Slim Fit","M","Blanco","Algodón","Larga","Cuello inglés",29.99,50,"Largo","Botones","Clásico")

print("Antes de las modificaciones:")
camisa.mostrar_informacion()

camisa.actualizar_precio(34.99)
camisa.largo_manga("antes de la muñeca")
camisa.cambiar_color("Azul")
camisa.cambiar_talla("L")
camisa.actualizar_material("Lino")
camisa.nueva_marca("lacoste")

print("\nDespués de las modificaciones:")
camisa.mostrar_informacion()
