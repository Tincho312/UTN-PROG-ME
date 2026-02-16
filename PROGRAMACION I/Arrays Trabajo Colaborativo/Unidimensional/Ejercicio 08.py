# Ejercicio 8: Encontrar Elementos Repetidos
# Escribe un programa que identifique y muestre los elementos que se repiten en una
# lista.
lista = [1, 2, 3, 2, 4, 5, 1, 6, 3]
repetidos = []
vistos = []
for elemento in lista:
    if elemento in vistos:
        if repetidos.count(elemento) == 0:
            repetidos.append(elemento)
    else:
        vistos.append(elemento)
print(f"Elementos que se repiten:{repetidos}")
