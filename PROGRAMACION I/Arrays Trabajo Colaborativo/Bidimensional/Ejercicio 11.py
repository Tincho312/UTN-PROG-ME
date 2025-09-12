# Ejercicio 11: Rotar una Matriz 90 Grados
# Escribe un programa que gire una lista bidimensional (matriz) 90 grados en el sentido
# de las agujas del reloj.


# Ingresamos el tamaño de la matriz
n = int(input("Ingrese el tamaño de la matriz: "))

# Ingresamos los elementos de la matriz
matriz = []
print("Ingrese los elementos de la matriz fila por fila:")
for i in range(n):
    fila = []
    for j in range(n):
        valor = int(input(f"Elemento [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

# Mostramos la matriz original
print("\nMatriz original:")
for fila in matriz:
    print(fila)

# Rotamos la matriz 90 grados en sentido horario
rotada = []
for j in range(n):
    nueva_fila = []
    for i in range(n - 1, -1, -1):  # recorremos desde la última fila hacia arriba
        nueva_fila.append(matriz[i][j])
    rotada.append(nueva_fila)

# Mostramos la matriz rotada
print("\nMatriz rotada 90° (horario):")
for fila in rotada:
    print(fila)
