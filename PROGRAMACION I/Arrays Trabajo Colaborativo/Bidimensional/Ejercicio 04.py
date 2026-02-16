"""
Escribe un programa que calcule la transpuesta de una matriz. La transpuesta de una
matriz intercambia sus filas por columnas.
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

# Imprimir la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

transpuesta = []

for j in range(columnas):
    filaTrans = []
    for i in range(filas):
        filaTrans.append(matriz[i][j])
    transpuesta.append(filaTrans)

# Imprimir la matriz transpuesta
print("")
print("Matriz transpuesta:")
for fila in transpuesta:
    print(fila)
