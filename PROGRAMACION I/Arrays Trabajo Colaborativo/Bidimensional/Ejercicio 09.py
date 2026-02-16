# Crea un programa que genere una matriz identidad inversa de tamaño n. Una matriz
# identidad inversa es una matriz cuadrada donde los elementos de la diagonal inversa
# principal son 1 y el resto son 0.

n = int(input("Ingrese el tamaño de la matriz: "))

matriz = []

for i in range(n):
    fila = []
    for j in range(n):
        if j == n - 1 - i:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)

for fila in matriz:
    print(fila)
