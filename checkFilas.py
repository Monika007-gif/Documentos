def checkFilas(sudoku):
    n = len(sudoku)
    numeros = list(range(1, n + 1))

    for fila in sudoku:
        if sorted(fila) != numeros:
            return False

    return True
