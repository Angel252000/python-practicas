class Ingreso:
    def __init__(self, cantidad, fecha, descripcion, categoria):
        self.cantidad = cantidad
        self.fecha = fecha
        self.descripcion = descripcion
        self.categoria = categoria

    def a_dict(self):
        return {
            "cantidad": self.cantidad,
            "fecha": self.fecha,
            "descripcion": self.descripcion,
            "categoria": self.categoria
        }
