def main():
    class Carro:
        def __init__(self, color, marca, modelo, año,placa,vehiculo_encendido):
            self.color = color
            self.marca = marca
            self.modelo = modelo
            self.año = año
            self.placa = placa
            self.vehiculo_encendido=vehiculo_encendido

        def mostrar_informacion(self):
            print("Marca:", self.marca)
            print("Modelo:", self.modelo)
            print("Año:", self.año)
            print("Color:", self.color)
            print("Placa:", self.placa)
            print("vehiculo_encendido:",self.vehiculo_encendido)

        
    mi_carro = Carro("azul", "Toyota", "Corolla", 2020,"MESSI_NEYMAR_SUAREZ","encendido")
    mi_carro.mostrar_informacion()

    class Persona:
        def __init__(self, nombre, edad, genero, ocupacion,telefono):
            self.nombre = nombre
            self.edad = edad
            self.genero = genero
            self.ocupacion = ocupacion
            self.telefono = telefono

        def mostrar_informacion(self):
            print("Nombre:", self.nombre)
            print("Edad:", self.edad)
            print("Género:", self.genero)
            print("Ocupación:", self.ocupacion)
            print("Teléfono:", self.telefono)
        
        
        def matricular_materia(self, materia):
            print(f"{self.nombre} se ha matriculado en {materia}")

    persona = Persona("Angel", 19, "Masculino", "Ingeniero","73229845")
    persona.mostrar_informacion()
    persona.matricular_materia("Matemáticas")

    persona = Persona("Angel", 19, "Masculino", "Ingeniero","73229845")
    persona.mostrar_informacion()

    class Materia:
         def __init__(self, nombre, aula, creditos, profesor, horario):
            self.nombre = nombre
            self.aula = aula
            self.creditos = creditos
            self.profesor = profesor
            self.horario = horario

         def mostrar_informacion(self):
           print("Nombre del curso:", self.nombre)
           print("Aula:", self.aula)
           print("Créditos:", self.creditos)
           print("Profesor:", self.profesor)
           print("Horario:", self.horario)

    materia = Materia("Matemáticas", "MATA6", 4, "Angel amaya","Lunes alas 6:30")
    materia.mostrar_informacion()

    class ProductoSupermercado:
        def __init__(self, nombre, precio, cantidad,calidad,marca):
            self.nombre = nombre
            self.precio = precio
            self.cantidad = cantidad 
            self.calidad = calidad
            self.marca = marca

        def mostrar_informacion(self):
            print("Producto:", self.nombre)
            print("Precio:", self.precio)
            print("Cantidad:", self.cantidad)
            print("Calidad:", self.calidad)
            print("Marca:", self.marca)

    def mostrar_productos_carro(carro):
        print("Productos en el carro:")
        for producto in carro:
            producto.mostrar_informacion()


    producto = ProductoSupermercado("Leche", 2.5, 1,"buena","La vaca lola")
    carro = [producto]
    mostrar_productos_carro(carro)

main()









        
       

