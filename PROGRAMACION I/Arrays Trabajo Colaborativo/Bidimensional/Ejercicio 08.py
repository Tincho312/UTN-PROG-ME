# Matriz Identidad

n = int(input("Ingresa el tamaño de la matriz identidad: "))

# Crear la matriz identidad
matriz_identidad = []
for i in range(n):
    fila = []
    for j in range(n):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    matriz_identidad.append(fila)

print("Matriz identidad de tamaño", n, ":")
for fila in matriz_identidad:
    print(fila)
