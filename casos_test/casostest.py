

from src.check_sudoku import check_sudoku
from tablero import (
    correcto,
    incorrecto1,
    incorrecto2,
    incorrecto3,
    incorrecto4,
    incorrecto5,
    incorrecto6,
)

assert check_sudoku(incorrecto1) == False
# >>> False

assert check_sudoku(correcto) == True
# >>> True

assert check_sudoku(incorrecto2) == False
# >>> False

assert check_sudoku(incorrecto3) == False
# >>> False

assert check_sudoku(incorrecto4) == False
# >>> False

assert check_sudoku(incorrecto5) == False
# >>> False

assert check_sudoku(incorrecto6) == False
# >>> False



# Pruebas de check_cuadrado
assert check_cuadrado(correcto) == True
assert check_cuadrado(incorrecto6) == False

# Pruebas de check_numeros_en_rango
assert check_numeros_en_rango(correcto) == True
assert check_numeros_en_rango(incorrecto2) == True

# Pruebas de check_filas
assert check_filas(correcto) == True
assert check_filas(incorrecto1) == False

# Pruebas de check_columnas
assert check_columnas(correcto) == True
assert check_columnas(incorrecto2) == False

# Pruebas de check_int
assert check_int(correcto) == True
assert check_int(incorrecto4) == False

print("Todas las pruebas se han superado correctamente.")
