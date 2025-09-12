# Ejercicio 10: Verificar Matriz Simétrica
# Una matriz es simétrica si es igual a su transpuesta. Escribe un programa que verifique
# si una matriz es simétrica.

# Usuario ingresa tamaño de matriz
n = int(input("Ingrese el tamaño de la matriz: "))

matriz = []

# cargo los elementos
print("Ingrese los elementos de la matriz fila por fila:")
for i in range(n):
    fila = []
    for j in range(n):
        valor = int(input(f"Elemento [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

# Muestro la matriz ingresada
print("\nMatriz ingresada:")
for fila in matriz:
    print(fila)

# Verificamos si hay simetría o no
simetrica = True
for i in range(n):
    for j in range(n):
        if matriz[i][j] != matriz[j][i]:
            simetrica = False
            break

# Resultado
if simetrica:
    print("\nLa matriz es simétrica.")
else:
    print("\nLa matriz NO es simétrica.")
