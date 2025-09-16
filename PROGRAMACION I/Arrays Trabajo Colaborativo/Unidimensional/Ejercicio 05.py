# Ejercicio 5: Multiplicar Elementos por un Valor
# Escribe un programa que multiplique cada elemento de una lista de números por un
# valor ingresado por el usuario
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
multiplicador = int(input("Ingrese un numero: "))
for num in numeros:
    print(num * multiplicador)
