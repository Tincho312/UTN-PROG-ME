# Escribe un programa que pida al usuario una lista de números y encuentre el mayor y
# el menor de ellos.
lista = []
opc = 1

while opc != 0:
    lista.append(int(input("Ingrese un valor Númerico: ")))
    print("¿Deseas Agregar Otro Número? ")
    opc = int(input("1: Agregar otro numero - 0: Salir "))

mayor = lista[0]
menor = lista[0]

for num in lista:
    if num > mayor:
        mayor = num
    if num < menor:
        menor = num

print("El valor minimo del arreglo es: ", menor)
print("El valor minimo del arreglo es: ", mayor)
