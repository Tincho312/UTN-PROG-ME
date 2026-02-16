# Ejercicio 13: Explique y ejemplifique la librería NumPy para trabajar con matrices y arrays

# ---La biblioteca NumPy es la opción recomendada para trabajar con matrices
# y arrays multidimensionales en Python.---

# EJEMPLOS BÁSICOS DE LA LIBRERÍA NUMPY

import numpy as np

# -------------------------------
# CREAR ARRAYS

# Vector unidimensional
a = np.array([1, 2, 3, 4, 5])
print("\nArray a:", a)

# Matriz bidimensional
b = np.array([[1, 2, 3], [4, 5, 6]])
print("Matriz b:\n", b)

# -------------------------------
# CREAR ARRAYS CON FUNCIONES

print("\nMatriz 3x3 de ceros:\n", np.zeros((3, 3)))
print("\nMatriz 2x4 de unos:\n", np.ones((2, 4)))
print("\nMatriz identidad 4x4:\n", np.eye(4))
print("\nArray de 1 a 9 con paso 2:", np.arange(1, 10, 2))

# -------------------------------
# OPERACIONES MATEMÁTICAS CON ARRAYS
x = np.array([1, 2, 3])
y = np.array([10, 20, 30])

print("\nSuma elemento a elemento x + y:", x + y)
print("Multiplicación elemento a elemento x * y:", x * y)
print("Potencia de x al cuadrado:", x**2)

# -------------------------------
# OPERACIONES CON MATRICES
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("\nSuma de matrices A + B:\n", A + B)
print("\nProducto matricial A @ B:\n", A @ B)
print("\nTranspuesta de A:\n", A.T)

# -------------------------------
# RELACIÓN CON LISTAS BIDIMENSIONALES
# Sumar todas las filas de una matriz con NumPy
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
suma_filas = matriz.sum(axis=1)
print("\nSuma de cada fila de la matriz:", suma_filas)
