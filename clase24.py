class Perfume:
    def __init__(self, marca, nombre, aroma, tipo_envase, volumen, duracion, tipo_fijacion, precio, cantidad_disponible, tipo_tapa, tipo_atomizador, presentacion):
        self.marca = marca
        self.nombre = nombre
        self.aroma = aroma
        self.tipo_envase = tipo_envase
        self.volumen = volumen
        self.duracion = duracion
        self.tipo_fijacion = tipo_fijacion
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible
        self.tipo_tapa = tipo_tapa
        self.tipo_atomizador = tipo_atomizador
        self.presentacion = presentacion

    def mostrar_informacion(self):
        print("Marca:", self.marca)
        print("Nombre:", self.nombre)
        print("Aroma:", self.aroma)
        print("Tipo de envase:", self.tipo_envase)
        print("Volumen:", self.volumen)
        print("Duración:", self.duracion)
        print("Tipo de fijación:", self.tipo_fijacion)
        print("Precio:", self.precio)
        print("Cantidad disponible:", self.cantidad_disponible)
        print("Tipo de tapa:", self.tipo_tapa)
        print("Tipo de atomizador:", self.tipo_atomizador)
        print("Presentación:", self.presentacion)

    def cambiar_precio(self, nuevo_precio):
        "Cambia el precio del perfume."
        self.precio = nuevo_precio

    def aumentar_stock(self, cantidad):
        "Aumenta la cantidad disponible en el stock."
        self.cantidad_disponible += cantidad

    def cambiar_aroma(self, nuevo_aroma):
        "Cambia el aroma del perfume."
        self.aroma = nuevo_aroma

    def cambiar_volumen(self, nuevo_volumen):
        "Cambia el volumen del perfume."
        self.volumen = nuevo_volumen

    def cambiar_tipo_envase(self, nuevo_tipo_envase):
        "Cambia el tipo de envase del perfume."
        self.tipo_envase = nuevo_tipo_envase

    def cambiar_presentacion(self, nueva_presentacion):
        "Cambia la presentación del perfume."
        self.presentacion = nueva_presentacion

perfume = Perfume("Chanel","Coco Mademoiselle","Floral","Frasco de vidrio","100 ml","8 horas","Agua de perfumen",120.00,50,"Spray","Recargable","Caja de lujo")

print("Información del perfume:")
perfume.mostrar_informacion()

perfume.cambiar_precio(130.00)
perfume.aumentar_stock(10)
perfume.cambiar_aroma("Oriental")
perfume.cambiar_volumen("50 ml")
perfume.cambiar_tipo_envase("Estuche compacto")
perfume.cambiar_presentacion("Edición limitada")

print("\nInformación actualizada del perfume:")
perfume.mostrar_informacion()

