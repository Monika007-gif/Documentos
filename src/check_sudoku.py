from src.check_columnas import check_columnas
from src.check_cuadrado import check_cuadrado
from src.check_filas import check_filas
from src.check_int import check_int
from src.check_numeros_en_rango import check_numeros_en_rango


def check_sudoku(sudoku):

    if not check_cuadrado(sudoku):
        return False

    if not check_int(sudoku):
        return False

    if not check_numeros_en_rango(sudoku):
        return False

    if not check_filas(sudoku):
        return False

    return check_columnas(sudoku)
      