# Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.


total = 0

while True:
    numero = int(input("Ingrese un número a sumar (0 para finalizar): "))

    if numero == 0:
        break

    total += numero

print("La suma total es:", total)
