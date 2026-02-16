# Ejercicio 7: Promedio de una Lista
# Escribe un programa que permita al usuario ingresar una lista de números y calcule el
# promedio de los elementos.
numeros = input("Ingresa una lista de números separados por espacios: ")
lista_numeros = [float(num) for num in numeros.split()]
promedio = sum(lista_numeros) / len(lista_numeros)
print(f"El promedio de los números ingresados es: {promedio}")
