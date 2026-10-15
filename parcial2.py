n = int(input("¿Cuántos números de la secuencia de Fibonacci quieres generar? "))

a, b = 0, 1
fibonacci_sequence = [a, b]

for _ in range(n - 2):
    a, b = b, a + b
    fibonacci_sequence.append(b)

print(fibonacci_sequence)

