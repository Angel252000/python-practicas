def main():
    def cuadrado(n):
        print("Cuadrado:")
        for i in range(1, n + 1):
            print(" ⬜ " * n)

    def triangulo_derecho(n):
        print("Triángulo derecho:")
        for i in range(1, n + 1):
            print(" ⬜ " * i)

    def diamante(n):
        print("Diamante:")
        for i in range(1, n + 1, 2):
         print(" " * ((n - i) // 2) + " ⬜ " * i)
        for i in range(n - 2, 0, -2):
         print(" " * ((n - i) // 2) + " ⬜ " * i)


    n = int(input("Ingrese un número impar mayor o igual que 2: "))

    if n < 2 and n % 2 == 0:
        print("El número debe ser mayor o igual que 2 pero impar.")
    else:
        cuadrado(n)
        triangulo_derecho(n)
        diamante(n)

main()



