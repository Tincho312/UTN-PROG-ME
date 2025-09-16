# Encontrar el Elemento Mayor

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 3, 2],
]

mayor = matriz[0][0] 
for fila in matriz:
    for elemento in fila:
        if elemento > mayor:
            mayor = elemento

print("El elemento mayor es:", mayor)