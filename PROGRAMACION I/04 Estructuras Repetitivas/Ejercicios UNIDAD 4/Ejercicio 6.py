# Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

numero = 100
while numero >= 0:
    if numero % 2 == 0:
        print(numero)
    numero -= 1
