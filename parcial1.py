def contador_frecuencia_palabras(texto):
    palabras = texto.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] = frecuencia[palabra] + 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

def registrar_palabra(frecuencia, palabra):
    if palabra in frecuencia:
        frecuencia[palabra] = frecuencia[palabra] + 1
    else:
        frecuencia[palabra] = 1
    return frecuencia

texto = "hola hola mundo mundo"
frecuencia_palabras = contador_frecuencia_palabras(texto)
print(frecuencia_palabras)

