class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def presentar(self):
        print(f'Soy {self.nombre}, tengo {self.edad} años, y soy {self.profesion}.')
