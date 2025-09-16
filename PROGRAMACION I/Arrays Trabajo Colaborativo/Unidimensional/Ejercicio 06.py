# Ejercicio 6: Eliminar Duplicados
# Escribe un programa que permita al usuario ingresar una lista de números y elimine los
# elementos duplicados.
entrada = input("Ingrese una lista de numeros: ")
numeros_str = entrada.split()
numeros = [int(num) for num in numeros_str]
numeros_sin_duplicados = set(numeros)
print(numeros_sin_duplicados)
