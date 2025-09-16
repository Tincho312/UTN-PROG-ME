"""
Crea una función que reciba dos parámetros: el número de filas y columnas. La función
debe generar una matriz de ese tamaño, donde los valores son números enteros
consecutivos empezando desde 1.
"""


# Función para generar la matriz
def generar_matriz(filas, columnas):
    matriz = []
    contador = 1
    for i in range(filas):
        fila = []  # Inicializa una nueva fila
        for j in range(columnas):
            fila.append(contador)  # Agrega el número consecutivo a la fila
            contador += 1
        matriz.append(fila)  # Agrega la fila a la matriz
    return matriz


# Programa principal
filas = 3
columnas = 3

matriz_generada = generar_matriz(filas, columnas)

for fila in matriz_generada:
    print(fila)
