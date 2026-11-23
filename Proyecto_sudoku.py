
# Comprueba que sea matriz cuadrada y que tenga al menos un elemento

def checkCuadrado(sudoku):

	n = len(sudoku)

	if n == 0:
		return False

	for fila in sudoku:
		if not isinstance(fila, list) or len(fila) != n:
			return False

	return True


# Comprueba que todos los números sean enteros y estén entre 1 y n.


def checkNumerosEnRango(sudoku):
    n = len(sudoku)

    for fila in sudoku:
        for numero in fila:
            if type(numero) != int or numero < 1 or numero > n:
                return False

    return True




# Comprueba que cada fila contenga todos los números sin repetir

def checkFilas(sudoku):
    n = len(sudoku)
    numeros = list(range(1, n + 1))

    for fila in sudoku:
        if sorted(fila) != numeros:
            return False

    return True


#Comprueba que las columnas tampoco tengan números repetidos

def checkColumnas(sudoku):
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

def checkInt(sudoku):
     for fila in sudoku:
        for numero in fila:
            if type (numero) != int:

             return False
     return True

# Comprueba que el sudoku sea válido

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




    #test_sudoku.py 

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


print(checkSudoku(incorrecto1))
# >>> False

print(checkSudoku(correcto))
# >>> True

print(checkSudoku(incorrecto2))
# >>> False

print(checkSudoku(incorrecto3))
# >>> False

print(checkSudoku(incorrecto4))
# >>> False

print(checkSudoku(incorrecto5))
# >>> False

print(checkSudoku(incorrecto6))
# >>> False



# PRUEBAS DE checkCuadrado()


print(checkCuadrado([[1, 2], [3, 4]]))
print(checkCuadrado([[1, 2, 3], [4, 5, 6]]))
print(checkCuadrado([]))
print(checkCuadrado([[1, 2], [3]]))
print(checkCuadrado([[1, 2], "hola"]))


# PRUEBAS DE checkNumerosEnRango()

print(checkNumerosEnRango([[1, 2], [2, 1]]))
print(checkNumerosEnRango([[1, 3], [2, 1]]))
print(checkNumerosEnRango([[1, 0], [2, 1]]))
print(checkNumerosEnRango([[1, 2], [2, 3]]))
print(checkNumerosEnRango([[1, 1.5], [2, 1]]))


print(checkFilas([[1, 2], [2, 1]]))
print(checkFilas([[1, 1], [2, 1]]))
print(checkFilas([[1, 2], [1, 1]]))
print(checkFilas([[2, 1], [1, 2]]))
print(checkFilas([[1, 3], [2, 1]]))
