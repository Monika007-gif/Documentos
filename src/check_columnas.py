def check_columnas(sudoku):
    n = len(sudoku)
    numeros = list(range(1, n + 1))

    for columna in range(n):
        valores = []

        for fila in range(n):
            valores.append(sudoku[fila][columna])

        if sorted(valores) != numeros:
            return False

    return True

