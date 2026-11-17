def checkNumerosEnRango(sudoku):
    n = len(sudoku)

    for fila in sudoku:
        for numero in fila:
            if type(numero) != int or numero < 1 or numero > n:
                return False

    return True

