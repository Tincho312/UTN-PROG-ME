# Escribe un programa que permita al usuario ingresar una lista de números y calcule la
# suma de todos los elementos en la lista.

lista = []
suma = 0
opc = 1

while opc != 0:
    lista.append(int(input("Ingrese un valor Númerico: ")))
    print("¿Deseas Agregar Otro Número? ")
    opc = int(input("1: Agregar otro numero - 0: Salir 5"))
suma = sum(lista)

print("La suma de los elementos es: ", suma)
