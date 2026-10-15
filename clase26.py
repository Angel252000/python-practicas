class Soda:
    def __init__(self, marca, sabor, volumen, color, azucar, cafeina, precio, cantidad_de_sodas, tipo_envase, estilo_tapa, estilo_etiqueta, carbonatada):
        self.marca = marca
        self.sabor = sabor
        self.volumen = volumen
        self.color = color
        self.azucar = azucar
        self.cafeina = cafeina
        self.precio = precio
        self.cantidad_de_sodas = cantidad_de_sodas
        self.tipo_envase = tipo_envase
        self.estilo_tapa = estilo_tapa
        self.estilo_etiqueta = estilo_etiqueta
        self.carbonatada = carbonatada

    def mostrar_informacion(self):
        print("Marca:", self.marca)
        print("Sabor:", self.sabor)
        print("Volumen:", self.volumen)
        print("Color:", self.color)
        print("Contenido de Azúcar:", self.azucar)
        print("Contenido de Cafeína:", self.cafeina)
        print("Precio:", self.precio)
        print("Cantidad de Sodas:", self.cantidad_de_sodas)
        print("Tipo de Envase:", self.tipo_envase)
        print("Estilo de Tapa:", self.estilo_tapa)
        print("Estilo de Etiqueta:", self.estilo_etiqueta)
        print("¿Es Carbonatada?:", self.carbonatada)

    def actualizar_precio(self, nuevo_precio):
        "Actualiza el precio de la soda."
        self.precio = nuevo_precio

    def cambiar_sabor(self, nuevo_sabor):
        "Cambia el sabor de la soda."
        self.sabor = nuevo_sabor

    def cambiar_volumen(self, nuevo_volumen):
        "Cambia el volumen de la soda."
        self.volumen = nuevo_volumen

    def cambiar_color(self, nuevo_color):
        "Cambia el color de la soda."
        self.color = nuevo_color

    def actualizar_tipo_envase(self, nuevo_tipo_envase):
        "Actualiza el tipo de envase de la soda."
        self.tipo_envase = nuevo_tipo_envase

    def actualizar_marca(self, nueva_marca):
        "Actualiza la marca de la soda."
        self.marca = nueva_marca


soda = Soda("Coca-Cola","Cola","355 ml","Marrón","39g","34 mg",5.50,100,"oro","Metálica","Estándar","si"
)

print("antes de saborear la mejor soda de todo el mundo :3:")
soda.mostrar_informacion()

soda.actualizar_precio(2.00)
soda.cambiar_sabor("explosion de menta")
soda.cambiar_color("Azul")
soda.cambiar_volumen("500 ml")
soda.actualizar_tipo_envase("Botella de Plástico")
soda.actualizar_marca("Menta pluss")

print("\ndespues de comprar para lo que me alcanzo con 2 dolares colones :( :")
soda.mostrar_informacion()
