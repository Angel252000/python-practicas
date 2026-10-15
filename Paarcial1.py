def contadorFrecuencia(cadena):
    frecuencia_palabras = {}
    palabras = cadena.lower().split()
    
    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1
    
    if frecuencia_palabras:
        palabra_mas_frecuente = max(frecuencia_palabras, key=frecuencia_palabras.get)
        print(f"Mayor frecuencia: {palabra_mas_frecuente}")
    
    return frecuencia_palabras

def main():
    testString = 'hola a todos hola'
    resultado = contadorFrecuencia(testString)
    print(resultado)

main()