# Diagonal de una Matriz Cuadrada

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 3, 2],
]

diagonal = []
for i in range(len(matriz)):
    diagonal.append(matriz[i][i])

print(diagonal)
