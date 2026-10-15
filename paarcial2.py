def main():
    def cuadrado(n):
        return [["* " * n for _ in range(1)] for _ in range(n)]

    def triangulo_derecho(n):
        return [["* " * i for _ in range(1)] for i in range(1, n + 1)]

    def diamante(n):
        result = [[" " * ((n - i) // 2) + "* " * i for _ in range(1)] for i in range(1, n + 1, 2)]
        result += [[" " * ((n - i) // 2) + "* " * i for _ in range(1)] for i in range(n - 2, 0, -2)]
        return result

    return cuadrado, triangulo_derecho, diamante

main()    