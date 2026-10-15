def contador_frecuencia_palabras(texto):
    palabras = texto.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

texto = "este es un ejemplo de un texto con palabras repetidas este es un ejemplo"
resultado = contador_frecuencia_palabras(texto)
print(resultado)

