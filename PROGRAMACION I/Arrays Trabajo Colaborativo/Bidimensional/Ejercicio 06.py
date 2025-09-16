# Multiplicar una Matriz por un Escalar

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 3, 2],
]

escalar = int(input("Ingresa un número escalar: "))

matriz_resultado = []
for fila in matriz:
    nueva_fila = []
    for elemento in fila:
        nueva_fila.append(elemento * escalar)
    matriz_resultado.append(nueva_fila)


print(matriz_resultado)
