def main():
    n = 10
    resultado = generar_fibonacci(n)
    print(resultado)

def generar_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fibonacci = [0, 1]
    for i in range(2, n):
        siguiente = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(siguiente)
    return fibonacci

main()
