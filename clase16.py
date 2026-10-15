def main():
    imprimir_cuadricula_inicial = input('Imprimir cuadricula inicial (y/n): ')
    n = int(input('Tamaño de la cuadrícula (impar): '))
    while n % 2 == 0:
        print("El tamaño debe ser un número impar.")
        n = int(input('Tamaño de la cuadrícula (impar): '))
        
    matrix = generar_cuadricula(n)
    
    if imprimir_cuadricula_inicial == 'y':
        imprimir_cuadricula(matrix)
    
    dibujar_X(matrix)
    imprimir_cuadricula(matrix)
    
    dibujar_cruz(matrix)
    print("\nCuadrícula con X y +:")
    imprimir_cuadricula(matrix)

def dibujar_X(grid):
    size = len(grid)
    for i in range(size):
        grid[i][i] = '⬛'
        grid[i][size - 1 - i] = '⬛'

def dibujar_cruz(grid):
    size = len(grid)
    centro = size // 2
    for i in range(size):
        if grid[centro][i] != '⬛':
            grid[centro][i] = '🟩'
        if grid[i][centro] != '⬛':
            grid[i][centro] = '🟩'

def imprimir_cuadricula(grid):
    size = len(grid)
    for i in range(size):
        if i != 0:
            print()
        for j in range(size):
            print(grid[i][j], end='')

def generar_cuadricula(size):
    return [['⬜️' for _ in range(size)] for _ in range(size)]

main()


