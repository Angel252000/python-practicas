def generar_cuadricula(size):
    return [['⬛' for _ in range(size)] for _ in range(size)]

def es_impar_mayor_o_igual_a_tres(n):
        return n >= 3 and n % 2 == 1

def dibujar_X(grid):
    size = len(grid)
    for i in range(size):
        grid[i][i] = '🟪'
        grid[i][size - 1 - i] = '🟪'

def dibujar_cruz(grid):
    size = len(grid)
    centro = size // 2
    for i in range(size):
        if grid[centro][i] != '⬛':
            grid[centro][i] = '🟩'
        if grid[i][centro] != '⬛':
            grid[i][centro] = '🟩'

def imprimir_cuadricula(grid):
    for row in grid:
        print(''.join(row))

