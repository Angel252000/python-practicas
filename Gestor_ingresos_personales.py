from categoria import Categoria
from ingreso import Ingreso
from presupuesto import Presupuesto


class GestorIngresosPersonales:
    def __init__(self):
        self.ingresos = []
        self.categorias = []
        self.presupuestos = []

    def añadir_ingreso(self, cantidad, fecha, descripcion, categoria):
        if categoria not in [categoria.nombre for categoria in self.categorias]:
            print(f"Error: La categoría '{categoria}' no existe. Por favor, añade la categoría primero.")
            return
        self.ingresos.append(Ingreso(cantidad, fecha, descripcion, categoria))

    def añadir_categoria(self, nombre):
        if nombre not in [categoria.nombre for categoria in self.categorias]:
            self.categorias.append(Categoria(nombre))
        else:
            print(f"La categoría '{nombre}' ya existe.")

    def añadir_presupuesto(self, cantidad, periodo):
        if periodo.lower() not in ["mensual", "anual"]:
            print("Error: El período debe ser 'mensual' o 'anual'.")
            return
        self.presupuestos.append(Presupuesto(cantidad, periodo))

    def generar_reporte(self):
        if not self.ingresos:
            print("No hay ingresos registrados.")
            return

        print("\nReporte de Ingresos:")
        for ingreso in self.ingresos:
            print(f"Fecha: {ingreso.fecha}, Cantidad: {ingreso.cantidad}, Descripción: {ingreso.descripcion}, Categoría: {ingreso.categoria}")

    def ver_ingresos(self):
        if not self.ingresos:
            print("No hay ingresos registrados.")
            return
        
        print("\nIngresos:")
        for ingreso in self.ingresos:
            print(f"Fecha: {ingreso.fecha}, Cantidad: {ingreso.cantidad}, Descripción: {ingreso.descripcion}, Categoría: {ingreso.categoria}")

    def ver_categorias(self):
        if not self.categorias:
            print("No hay categorías registradas.")
            return
        
        print("\nCategorías:")
        for categoria in self.categorias:
            print(f"- {categoria.nombre}")

    def ver_presupuestos(self):
        if not self.presupuestos:
            print("No hay presupuestos registrados.")
            return

        print("\nPresupuestos:")
        for presupuesto in self.presupuestos:
            print(f"Período: {presupuesto.periodo}, Cantidad: {presupuesto.cantidad}")
