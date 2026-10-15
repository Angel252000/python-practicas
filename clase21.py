class Planta:
    def __init__(self, nombre_cientifico, nombre_comun, familia, origen, altura_maxima, clima_ideal, tipo_suelo, riego, exposicion_solar, epoca_floracion, cuidados_especiales, cantidad):
        self.nombre_cientifico = nombre_cientifico
        self.nombre_comun = nombre_comun
        self.familia = familia
        self.origen = origen
        self.altura_maxima = altura_maxima
        self.clima_ideal = clima_ideal
        self.tipo_suelo = tipo_suelo
        self.riego = riego
        self.exposicion_solar = exposicion_solar
        self.epoca_floracion = epoca_floracion
        self.cuidados_especiales = cuidados_especiales
        self.cantidad = cantidad

    def mostrar_informacion(self):
        print("Nombre Científico:", self.nombre_cientifico)
        print("Nombre Común:", self.nombre_comun)
        print("Familia:", self.familia)
        print("Origen:", self.origen)
        print("Altura Máxima:", self.altura_maxima)
        print("Clima Ideal:", self.clima_ideal)
        print("Tipo de Suelo:", self.tipo_suelo)
        print("Riego:", self.riego)
        print("Exposición Solar:", self.exposicion_solar)
        print("Época de Floración:", self.epoca_floracion)
        print("Cuidados Especiales:", self.cuidados_especiales)
        print("Cantidad en el Jardín:", self.cantidad)

    def actualizar_clima_ideal(self, nuevo_clima):
        """Actualiza el clima ideal para la planta."""
        self.clima_ideal = nuevo_clima

    def aumentar_cantidad(self, cantidad_adicional):
        """Aumenta la cantidad de plantas en el jardín."""
        self.cantidad += cantidad_adicional

    def cambiar_tipo_suelo(self, nuevo_suelo):
        """Cambia el tipo de suelo donde se cultiva la planta."""
        self.tipo_suelo = nuevo_suelo

    def actualizar_riego(self, nuevo_riego):
        """Actualiza la frecuencia de riego de la planta."""
        self.riego = nuevo_riego

    def cambiar_exposicion_solar(self, nueva_exposicion):
        """Cambia la exposición solar requerida para la planta."""
        self.exposicion_solar = nueva_exposicion

    def actualizar_cuidados_especiales(self, nuevos_cuidados):
        """Actualiza los cuidados especiales necesarios para la planta."""
        self.cuidados_especiales = nuevos_cuidados

    def cambiar_epoca_floracion(self, nueva_epoca):
        """Cambia la época de floración de la planta."""
        self.epoca_floracion = nueva_epoca


planta = Planta("Rosa chinensis","Rosa de China","Rosaceae","Asia","1.5 m","Templado","Franco","Moderado","Pleno sol","Primavera","Poda regular",10)

print("Antes de las modificaciones:")
planta.mostrar_informacion()

planta.actualizar_clima_ideal("Subtropical")
planta.aumentar_cantidad(5)
planta.cambiar_tipo_suelo("Arenoso")
planta.actualizar_riego("Frecuente")
planta.cambiar_exposicion_solar("Sombra parcial")
planta.actualizar_cuidados_especiales("Protección contra heladas")
planta.cambiar_epoca_floracion("Verano")

print("\nDespués de las modificaciones:")
planta.mostrar_informacion()
