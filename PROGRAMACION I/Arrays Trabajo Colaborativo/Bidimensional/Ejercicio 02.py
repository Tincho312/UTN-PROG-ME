"""
Escribe un programa que calcule la suma de todos los elementos en una lista
bidimensional.
Pista: Aplique la función sum
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

# Calcular la suma de todos los elementos en la matriz
suma_total = sum(sum(fila) for fila in matriz)
print("La suma de todos los elementos en la matriz es:", suma_total)
