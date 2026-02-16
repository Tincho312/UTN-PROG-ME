# Ejercicio 11: Contar Ocurrencias de un Elemento
# Escribe un programa que permita al usuario ingresar una lista y un número, y cuente
# cuántas veces aparece ese número en la lista.

entrada = input("Ingresa números separados por comas: ")
numeros = [int(x) for x in entrada.split(",")]

# Pedir el número a contar
numero_a_contar = int(input("Ingresa el número a contar: "))

# Contar las ocurrencias
cantidad = numeros.count(numero_a_contar)

# Mostrar el resultado
print(f"El número {numero_a_contar} aparece {cantidad} veces en la lista.")
