import unittest

from paarcial3 import generar_cuadricula, dibujar_X, dibujar_cruz


def test_es_impar_mayor_o_igual_a_tres():
    assert test_es_impar_mayor_o_igual_a_tres(3) == True
    assert test_es_impar_mayor_o_igual_a_tres(4) == False
    assert test_es_impar_mayor_o_igual_a_tres(5) == True
    assert test_es_impar_mayor_o_igual_a_tres(2) == False
    assert test_es_impar_mayor_o_igual_a_tres(7) == True

def test_generar_cuadricula3x3():
    grid = generar_cuadricula(3)
    expected_grid = [
        ['⬛', '⬛', '⬛'],
        ['⬛', '⬛', '⬛'],
        ['⬛', '⬛', '⬛']
    ]
    assert grid == expected_grid

def test_generar_cuadricula5x5():
    grid = generar_cuadricula(5)
    expected_grid = [
        ['⬛', '⬛', '⬛', '⬛', '⬛'],
        ['⬛', '⬛', '⬛', '⬛', '⬛'],
        ['⬛', '⬛', '⬛', '⬛', '⬛'],
        ['⬛', '⬛', '⬛', '⬛', '⬛'],
        ['⬛', '⬛', '⬛', '⬛', '⬛']
    ]
    assert grid == expected_grid

def test_generar_cuadricula7x7():
    grid = generar_cuadricula(7)
    expected_grid = [
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛'],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛'],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛'],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛'],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛'],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛'],
        ['⬛', '⬛', '⬛', '⬛', '⬛', '⬛', '⬛']
    ]
    assert grid == expected_grid


def test_dibujar_X_3x3():
    grid = generar_cuadricula(3)
    dibujar_X(grid)
    expected_grid = [
        ['🟪', '⬛', '🟪'],
        ['⬛', '🟪', '⬛'],
        ['🟪', '⬛', '🟪']
    ]
    assert grid == expected_grid

def test_dibujar_X_5x5():
    grid = generar_cuadricula(5)
    dibujar_X(grid)
    expected_grid = [
        ['🟪', '⬛', '⬛', '⬛', '🟪'],
        ['⬛', '🟪', '⬛', '🟪', '⬛'],
        ['⬛', '⬛', '🟪', '⬛', '⬛'],
        ['⬛', '🟪', '⬛', '🟪', '⬛'],
        ['🟪', '⬛', '⬛', '⬛', '🟪']
    ]
    assert grid == expected_grid

def test_dibujar_X_7x7():
    grid = generar_cuadricula(7)
    dibujar_X(grid)
    expected_grid = [
        ['🟪', '⬛', '⬛', '⬛', '⬛', '⬛', '🟪'],
        ['⬛', '🟪', '⬛', '⬛', '⬛', '🟪', '⬛'],
        ['⬛', '⬛', '🟪', '⬛', '🟪', '⬛', '⬛'],
        ['⬛', '⬛', '⬛', '🟪', '⬛', '⬛', '⬛'],
        ['⬛', '⬛', '🟪', '⬛', '🟪', '⬛', '⬛'],
        ['⬛', '🟪', '⬛', '⬛', '⬛', '🟪', '⬛'],
        ['🟪', '⬛', '⬛', '⬛', '⬛', '⬛', '🟪']
    ]
    assert grid == expected_grid

def test_dibujar_cruz_3x3():
    grid = generar_cuadricula(3)
    dibujar_X(grid)
    dibujar_cruz(grid)
    expected_grid = [
        ['🟪', '🟩', '🟪'],
        ['🟩', '🟩', '🟩'],
        ['🟪', '🟩', '🟪']
    ]
    assert grid == expected_grid

def test_dibujar_cruz_5x5():
    grid = generar_cuadricula(5)
    dibujar_X(grid)
    dibujar_cruz(grid)
    expected_grid = [
        ['🟪', '⬛', '🟩', '⬛', '🟪'],
        ['⬛', '🟪', '🟩', '🟪', '⬛'],
        ['🟩', '🟩', '🟩', '🟩', '🟩'],
        ['⬛', '🟪', '🟩', '🟪', '⬛'],
        ['🟪', '⬛', '🟩', '⬛', '🟪']
    ]
    assert grid == expected_grid

def test_dibujar_cruz_7x7():
    grid = generar_cuadricula(7)
    dibujar_X(grid)
    dibujar_cruz(grid)
    expected_grid = [
        ['🟪', '⬛', '⬛', '🟩', '⬛', '⬛', '🟪'],
        ['⬛', '🟪', '⬛', '🟩', '⬛', '🟪', '⬛'],
        ['⬛', '⬛', '🟪', '🟩', '🟪', '⬛', '⬛'],
        ['🟩', '🟩', '🟩', '🟩', '🟩', '🟩', '🟩'],
        ['⬛', '⬛', '🟪', '🟩', '🟪', '⬛', '⬛'],
        ['⬛', '🟪', '⬛', '🟩', '⬛', '🟪', '⬛'],
        ['🟪', '⬛', '⬛', '🟩', '⬛', '⬛', '🟪']
    ]
    assert grid == expected_grid