# Ejercicio 12: Sumar Listas Elemento por Elemento
# Escribe un programa que sume dos listas de números elemento por elemento. Las
# listas deben tener la misma longitud.
# Pedir al usuario la primera lista de números
entrada1 = input("Ingresa los números de la primera lista separados por comas: ")
lista1 = [int(x) for x in entrada1.split(",")]

# Pedir al usuario la segunda lista de números
entrada2 = input("Ingresa los números de la segunda lista separados por comas: ")
lista2 = [int(x) for x in entrada2.split(",")]

# Verificar que las listas tengan la misma longitud
if len(lista1) != len(lista2):
    print("Error: Las listas no tienen la misma longitud.")
else:
    # Sumar elemento por elemento
    suma = [a + b for a, b in zip(lista1, lista2)]
    print("Lista resultante de la suma:", suma)
