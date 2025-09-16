"""
Modifica el programa anterior para que imprima la suma de cada fila de la lista
bidimensional.
"""

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))
matriz = []
contador = 1

# Crear la matriz con números secuenciales
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(contador)
        contador += 1
    matriz.append(fila)

# Calcular la suma de todos los elementos de cada fila e imprimirla
for fila in matriz:
    print(f"La suma de la fila {fila} es:", sum(fila))
