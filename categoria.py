
class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

    def a_dict(self):
        return {"nombre": self.nombre}
