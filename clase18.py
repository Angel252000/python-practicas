def main():
    import random

    TAMAÑO_TABLERO = 10
    NUM_NAVES = 7
    MAX_TURNOS = 21

    tablero = [['⬛' for _ in range(TAMAÑO_TABLERO)] for _ in range(TAMAÑO_TABLERO)]

    naves = 0
    while naves < NUM_NAVES:
        x = random.randint(0, TAMAÑO_TABLERO - 1)
        y = random.randint(0, TAMAÑO_TABLERO - 1)
        if tablero[x][y] == '⬛':
            tablero[x][y] = '🟨'
            naves += 1

    turnos = 0
    naves_hundidas = 0

    while turnos < MAX_TURNOS and naves_hundidas < NUM_NAVES:
        print(f"Turno {turnos + 1}")

        for fila in tablero:
            print("".join(fila))

        x = int(input("Introduce coordenada X (0-9): "))
        y = int(input("Introduce coordenada Y (0-9): "))

        if tablero[x][y] == '🟨':
            print(f"¡Hundiste una nave en la coordenada ({x}, {y})!")
            tablero[x][y] = '🟥'
            naves_hundidas += 1
        elif tablero[x][y] == '⬛':
            print("Disparo fallido. No hay ninguna nave en esa coordenada.")
            tablero[x][y] = '❌'
        else:
            print("Ya disparaste en esa coordenada.")

        turnos += 1

    if naves_hundidas == NUM_NAVES:
        print("¡Ganaste! Hundiste todas las naves.")
    else:
        print("No ganaste. No lograste hundir todas las naves en 21 turnos.")

    for fila in tablero:
        print("".join(fila))

main()
