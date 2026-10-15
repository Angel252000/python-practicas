def main():
    def es_impar_mayor_o_igual_a_tres(n):
        return n >= 3 and n % 2 == 1

    def generar_cuadricula(n):
        cuadricula = [['🟥' for _ in range(n)] for _ in range(n)]
        return cuadricula

    def imprimir_cuadricula(cuadricula):
        for fila in cuadricula:
            for elemento in fila:
                print(elemento, end='')
            print()
        print()

    def dibujar_triangulo(cuadricula, n):
        medio = n // 2
        for i in range(medio + 1):
            for j in range(medio - i, medio + i + 1):
                cuadricula[i][j] = '🟩'

    while True:
        num = int(input("Introduce un número impar mayor o igual a 3: "))
        if es_impar_mayor_o_igual_a_tres(num):
            break
        else:
            print("El número no es válido. Inténtalo de nuevo.")
    
    cuadricula = generar_cuadricula(num)
    imprimir_cuadricula(cuadricula)
    dibujar_triangulo(cuadricula, num)
    imprimir_cuadricula(cuadricula)

main()


