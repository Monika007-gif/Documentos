
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


assert (checkSudoku(incorrecto1)) == False
# >>> False

assert (checkSudoku(correcto)) == True
# >>> True

assert (checkSudoku(incorrecto2)) == False
# >>> False

assert (checkSudoku(incorrecto3)) == False
# >>> False

assert (checkSudoku(incorrecto4)) == False
# >>> False

assert (checkSudoku(incorrecto5)) == False
# >>> False

assert (checkSudoku(incorrecto6)) == False
# >>> False



# PRUEBAS DE checkCuadrado()


assert(checkCuadrado([[1, 2], [3, 4]])) == True
assert(checkCuadrado([[1, 2, 3], [4, 5, 6]])) == False
assert(checkCuadrado([])) == True
assert(checkCuadrado([[1, 2], [3]])) == False
assert(checkCuadrado([[1, 2], "hola"])) == False

# PRUEBAS DE checkNumerosEnRango()

assert(checkNumerosEnRango([[1, 2], [2, 1]])) == True
assert(checkNumerosEnRango([[1, 3], [2, 1]])) == False
assert(checkNumerosEnRango([[1, 0], [2, 1]])) == False
assert(checkNumerosEnRango([[1, 2], [2, 3]])) == False
assert(checkNumerosEnRango([[1, 1.5], [2, 1]])) == False


assert(checkFilas([[1, 2], [2, 1]])) == True
assert(checkFilas([[1, 1], [2, 1]])) == False
assert(checkFilas([[1, 2], [1, 1]])) == False
assert(checkFilas([[2, 1], [1, 2]])) == False
assert(checkFilas([[1, 3], [2, 1]])) == False


assert(checkColumnas([[1, 2], [2, 1]])) == True
assert(checkColumnas([[1, 1], [2, 1]])) == False
assert(checkColumnas([[1, 2], [1, 1]])) == False
assert(checkColumnas([[2, 1], [1, 2]])) == False
assert(checkColumnas([[1, 3], [2, 1]])) == False


# PRUEBAS DE checkInt()
assert(checkInt([[1, 2], [2, 1]])) == True
assert(checkInt([[1, 1.5], [2, 1]])) == False
assert(checkInt([["a", 2], [2, 1]])) == False
assert(checkInt([[0, -1], [2, 1]])) == False
assert(checkInt([[1, 2], [3, 4]])) == True



assert(checkSudoku([[1, 2, 3], [2, 3, 1], [3, 1, 2]])) == True
assert(checkSudoku([[1, 2, 3, 4], [2, 3, 1, 3], [3, 1, 2, 3], [4, 4, 4, 4]])) == False
assert(checkSudoku([[1, 2, 3, 4], [2, 3, 1, 4], [4, 1, 2, 3], [3, 4, 1, 2]])) == False
assert(checkSudoku([["a", "b", "c"], ["b", "c", "a"], ["c", "a", "b"]])) == False
assert(checkSudoku([[1, 1.5], [1.5, 1]])) == False


# Si quiero comprobar por separado sin usar comentarios, para no ejecuar todos los casos test, hago lo siguiente:

# if __name__ == "__main__":
# test_checkCuadrado() para el cuadrado, por ejemplo.

# Al final del archivo.
