class Maleta:
    def __init__(self, marca, material, color, peso_vacia, dimensiones, capacidad, tipo_cierre, cantidad_ruedas, asa_telescópica, bolsillos_interiores, resistente_agua, precio):
        self.marca = marca
        self.material = material
        self.color = color
        self.peso_vacia = peso_vacia
        self.dimensiones = dimensiones
        self.capacidad = capacidad
        self.tipo_cierre = tipo_cierre
        self.cantidad_ruedas = cantidad_ruedas
        self.asa_telescópica = asa_telescópica
        self.bolsillos_interiores = bolsillos_interiores
        self.resistente_agua = resistente_agua
        self.precio = precio

    def mostrar_informacion(self):
        print("Marca:", self.marca)
        print("Material:", self.material)
        print("Color:", self.color)
        print("Peso (vacía):", self.peso_vacia)
        print("Dimensiones:", self.dimensiones)
        print("Capacidad:", self.capacidad)
        print("Tipo de cierre:", self.tipo_cierre)
        print("Cantidad de ruedas:", self.cantidad_ruedas)
        print("Asa telescópica:", self.asa_telescópica)
        print("Bolsillos interiores:", self.bolsillos_interiores)
        print("Resistente al agua:", self.resistente_agua)
        print("Precio:", self.precio)

    def cambiar_color(self, nuevo_color):
        "Cambia el color de la maleta."
        self.color = nuevo_color

    def aumentar_capacidad(self, aumento):
        "Aumenta la capacidad de la maleta."
        self.capacidad += aumento

    def agregar_bolsillo_interior(self, nuevo_bolsillo):
        "Agrega un bolsillo interior a la maleta."
        self.bolsillos_interiores.append(nuevo_bolsillo)

    def cambiar_precio(self, nuevo_precio):
        "Cambia el precio de la maleta."
        self.precio = nuevo_precio

    def ajustar_asa_telescópica(self, nueva_longitud):
        "Ajusta la longitud de la asa telescópica."
        self.asa_telescópica = nueva_longitud

    def hacer_resistente_agua(self):
        "Hace que la maleta sea resistente al agua."
        self.resistente_agua = True

maleta = Maleta(
    "Samsonite","Poliéster","Negro","3.5 kg","20x40x60 cm","60 L","Cremallera",4,"si",["Bolsillo con cremallera", "Bolsillo para documentos"],"no",150.00)

print("Información de la maleta:")
maleta.mostrar_informacion()

maleta.cambiar_color("Azul")
maleta.aumentar_capacidad(10)
maleta.agregar_bolsillo_interior("Bolsillo para laptop")
maleta.cambiar_precio(180.00)
maleta.ajustar_asa_telescópica("110 cm")
maleta.hacer_resistente_agua()

print("\nInformación actualizada de la maleta:")
maleta.mostrar_informacion()
