# Proyecto Sudoku

## Descripción

Este proyecto consiste en un programa desarrollado con Python, permite comprobar si una matriz cumple las condiciones necesarias para ser considerada un Sudoku válido.

El programa realiza diferentes comprobaciones sobre la matriz, para verificar que su estructura y sus valores sean correctos.

## Funcionalidades

El programa incluye las siguientes funciones:

checkCuadrado(sudoku): comprueba que la matriz sea cuadrada.

checkNumerosEnRango(sudoku): comprueba que los números estén dentro del rango permitido.

checkFilas(sudoku): comprueba que cada fila contenga los números sin repetir.

checkColumnas(sudoku): comprueba que cada columna contenga los números sin repetir.

checkInt(sudoku): comprueba que todos los valores sean números enteros.

checkSudoku(sudoku): reúne todas las comprobaciones anteriores y determina si el Sudoku es válido.

## Requisitos

Tener Python 3 instalado y tener un editor de código.

No es necesario instalar librerías externas.


Descargar o clonar el repositorio.

Abrir la carpeta del proyecto.

Ejecutar el archivo principal desde la terminal:

python3 Proyecto_sudoku.py

El programa ejecutará las pruebas definidas mediante assert para comprobar que las funciones funcionan correctamente.

Pruebas

El proyecto incluye pruebas mediante instrucciones assert, que permiten verificar el comportamiento de las funciones con diferentes matrices.

Si todas las pruebas se ejecutan correctamente, el programa finalizará sin mostrar errores. Si alguna prueba falla, Python mostrará un error indicando qué comprobación no se ha superado.

Autoría

Proyecto realizado como ejercicio de programación en Python.