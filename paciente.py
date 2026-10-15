from animal import Animal

class Paciente(Animal):
    def __init__(self, tipo, raza, color, edad, nombre, nombre_representante, telefono, correo, direccion):
        super().__init__(tipo, raza, color, edad)
        self.nombre = nombre
        self.nombre_representante = nombre_representante
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.consultas = []