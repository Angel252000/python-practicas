class Presupuesto:
    def __init__(self, cantidad, periodo):
        self.cantidad = cantidad
        self.periodo = periodo

    def a_dict(self):
        return {
            "cantidad": self.cantidad,
            "periodo": self.periodo
        }
