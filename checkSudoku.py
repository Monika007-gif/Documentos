def checkSudoku(sudoku):

    if not checkCuadrado(sudoku):
        return False

    if not checkInt(sudoku):
        return False

    if not checkNumerosEnRango(sudoku):
        return False

    if not checkFilas(sudoku):
        return False

    if not checkColumnas(sudoku):
       return False

       return True

