class Libro:
    def __init__(self, titulo, autor, genero, editorial, idioma, año_publicacion, paginas, precio, cantidad_disponible, formato, isbn, sinopsis):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.editorial = editorial
        self.idioma = idioma
        self.año_publicacion = año_publicacion
        self.paginas = paginas
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible
        self.formato = formato
        self.isbn = isbn
        self.sinopsis = sinopsis

    def mostrar_informacion(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Género:", self.genero)
        print("Editorial:", self.editorial)
        print("Idioma:", self.idioma)
        print("Año de Publicación:", self.año_publicacion)
        print("Número de Páginas:", self.paginas)
        print("Precio:", self.precio)
        print("Cantidad Disponible:", self.cantidad_disponible)
        print("Formato:", self.formato)
        print("ISBN:", self.isbn)
        print("Sinopsis:", self.sinopsis)

    def actualizar_precio(self, nuevo_precio):
        "Actualiza el precio del libro."
        self.precio = nuevo_precio

    def cambiar_autor(self, nuevo_autor):
        "Cambia el autor del libro."
        self.autor = nuevo_autor

    def cambiar_genero(self, nuevo_genero):
        "Cambia el género del libro."
        self.genero = nuevo_genero

    def cambiar_editorial(self, nueva_editorial):
        "Cambia la editorial del libro."
        self.editorial = nueva_editorial

    def cambiar_cantidad_disponible(self, nueva_cantidad):
        "Cambia la cantidad disponible del libro."
        self.cantidad_disponible = nueva_cantidad

    def cambiar_sinopsis(self, nueva_sinopsis):
        "Cambia la sinopsis del libro."
        self.sinopsis = nueva_sinopsis

libro = Libro("Cien años de soledad","Gabriel García Márquez","Realismo mágico","Sudamericana","Español",1967,432,25.00,100,"Tapa blanda","978-0307350365","La novela narra la historia de la familia Buendía a lo largo de siete generaciones en el pueblo ficticio de Macondo.")

print("Antes de estar solo:")
libro.mostrar_informacion()

libro.actualizar_precio(30.00)
libro.cambiar_autor("Isabel Allende")
libro.cambiar_genero("Novela histórica")
libro.cambiar_cantidad_disponible(80)
libro.cambiar_sinopsis("La historia de amor entre Esteban Trueba y Clara del Valle en un contexto de cambios políticos en Chile.")
libro.cambiar_editorial("Plaza & Janés")

print("\nDespues de quedarme solo:")
libro.mostrar_informacion()
