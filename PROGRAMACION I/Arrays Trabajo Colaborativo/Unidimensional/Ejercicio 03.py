# Escribe un programa que permita al usuario ingresar una lista y la invierta.

lista = []

print("Ingresa los elementos uno por uno. Escribe 'fin' para terminar.")

while True:
    entrada = input("Ingresa un elemento: ")
    if entrada.lower() == "fin":
        break
    lista.append(entrada)

lista.reverse()

print("Lista invertida:", lista)
