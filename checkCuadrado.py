def checkCuadrado(sudoku):

	n = len(sudoku)

	if n == 0:
		return False

	for fila in sudoku:
		if not isinstance(fila, list) or len(fila) != n:
			return False

	return True
