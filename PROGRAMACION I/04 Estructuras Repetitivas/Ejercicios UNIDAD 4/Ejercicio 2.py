# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero = int(input("Ingrese un Número: "))
contador = 0
n = abs(numero)

while n > 0:
    n = n // 10
    contador += 1

if numero == 0:
    contador += 1

print("El Número contiene", contador, "digitos")
