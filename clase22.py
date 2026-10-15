class Carro:
    def __init__(self, marca, modelo, año, color, tipo_motor, combustible, transmision, puertas, capacidad_pasajeros, kilometraje, traccion, peso, longitud):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.tipo_motor = tipo_motor
        self.combustible = combustible
        self.transmision = transmision
        self.puertas = puertas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.kilometraje = kilometraje
        self.traccion = traccion
        self.peso = peso
        self.longitud = longitud

    def mostrar_informacion(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Año:", self.año)
        print("Color:", self.color)
        print("Tipo de Motor:", self.tipo_motor)
        print("Combustible:", self.combustible)
        print("Transmisión:", self.transmision)
        print("Puertas:", self.puertas)
        print("Capacidad de Pasajeros:", self.capacidad_pasajeros)
        print("Kilometraje:", self.kilometraje)
        print("Tracción:", self.traccion)
        print("Peso:", self.peso)
        print("Longitud:", self.longitud)

    def actualizar_color(self, nuevo_color):
        "Actualiza el color de carro."
        self.color = nuevo_color

    def actualizar_kilometraje(self, nuevo_kilometraje):
        "Actualiza el kilometraje de carro."
        self.kilometraje = nuevo_kilometraje

    def cambiar_tipo_motor(self, nuevo_tipo_motor):
        "Cambia el tipo de motor de carro."
        self.tipo_motor = nuevo_tipo_motor

    def actualizar_combustible(self, nuevo_combustible):
        "Actualiza el tipo de combustible de carro."
        self.combustible = nuevo_combustible

    def cambiar_transmision(self, nueva_transmision):
        "Cambia la transmisión de carro."
        self.transmision = nueva_transmision
    
    def cambiar_marca(self, nueva_marca):
        "Cambia la marca de carro."
        self.nueva_marca = nueva_marca

carro = Carro("Toyota","Corolla",2020,"Rojo","1.8L I4","Gasolina","Automática",4,5,15000,"Delantera",1200,4.5)

print("Antes de ser Torreto:")
carro.mostrar_informacion()

carro.actualizar_color("Azul")
carro.actualizar_kilometraje(20000)
carro.cambiar_tipo_motor("2.0L I4")
carro.actualizar_combustible("Híbrido")
carro.cambiar_transmision("Manual")
carro.cambiar_marca("tesla")

print("\nDespués de ser Torreto la familia es primero :")
carro.mostrar_informacion()
