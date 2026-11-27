
# Comprueba que sea matriz cuadrada y que tenga al menos un elemento

def check_cuadrado(sudoku):

	n = len(sudoku)

	if n == 0:
		return False

	for fila in sudoku:
		if not isinstance(fila, list) or len(fila) != n:
			return False

	return True


# Comprueba que todos los números sean enteros y estén entre 1 y n.


def check_numeros_en_rango(sudoku):
    n = len(sudoku)

    for fila in sudoku:
        for numero in fila:
            if type(numero) != int or numero < 1 or numero > n:
                return False

    return True




# Comprueba que cada fila contenga todos los números sin repetir

def check_filas(sudoku):
    n = len(sudoku)
    numeros = list(range(1, n + 1))

    for fila in sudoku:
        if sorted(fila) != numeros:
            return False

    return True


#Comprueba que las columnas tampoco tengan números repetidos

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



# comprueba que todos los elementos sean enteros

def check_int(sudoku):
    for fila in sudoku:
        for numero in fila:
            if type (numero) != int:

             return False
    return True

# Comprueba que el sudoku sea válido

def check_sudoku(sudoku):

    if not check_cuadrado(sudoku):
        return False

    if not check_int(sudoku):
        return False

    if not check_numeros_en_rango(sudoku):
        return False

    if not check_filas(sudoku):
        return False

    check_columnas(sudoku)
        
    




    # pruebas del programa 

correcto = [[1, 2, 3],
            [2, 3, 1],
            [3, 1, 2]]

incorrecto1 = [[1, 2, 3, 4],
               [2, 3, 1, 3],
               [3, 1, 2, 3],
               [4, 4, 4, 4]]

incorrecto2 = [[1, 2, 3, 4],
               [2, 3, 1, 4],
               [4, 1, 2, 3],
               [3, 4, 1, 2]]

incorrecto3 = [[1, 2, 3, 4, 5],
               [2, 3, 1, 5, 6],
               [4, 5, 2, 1, 3],
               [3, 4, 5, 2, 1],
               [5, 6, 4, 3, 2]]

incorrecto4 = [['a', 'b', 'c'],
               ['b', 'c', 'a'],
               ['c', 'a', 'b']]

incorrecto5 = [[1, 1.5],
               [1.5, 1]]

incorrecto6 = [[1, 0, 0, 0],
               [0, 1, 0],
               [0, 0, 0, 1]]



assert checkSudoku(incorrecto1) == False
# >>> False

assert checkSudoku(correcto) == True
# >>> True

assert checkSudoku(incorrecto2) == False
# >>> False

assert checkSudoku(incorrecto3) == False
# >>> False

assert checkSudoku(incorrecto4) == False
# >>> False

assert checkSudoku(incorrecto5) == False
# >>> False

assert checkSudoku(incorrecto6) == False
# >>> False



# Pruebas de checkCuadrado
assert checkCuadrado(correcto) == True
assert checkCuadrado(incorrecto6) == False

# Pruebas de checkNumerosEnRango
assert checkNumerosEnRango(correcto) == True
assert checkNumerosEnRango(incorrecto2) == True

# Pruebas de checkFilas
assert checkFilas(correcto) == True
assert checkFilas(incorrecto1) == False

# Pruebas de checkColumnas
assert checkColumnas(correcto) == True
assert checkColumnas(incorrecto2) == False

# Pruebas de checkInt
assert checkInt(correcto) == True
assert checkInt(incorrecto4) == False

print("Todas las pruebas se han superado correctamente.")
