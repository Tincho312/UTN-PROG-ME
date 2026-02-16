# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares = 0
impares = 0
positivos = 0
negativos = 0
cantidad_numeros = 100

for i in range(cantidad_numeros):
    numero = int(input("Ingrese un número : "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(
    "Números pares:",
    pares,
    "Números impares:",
    impares,
    "Números positivos:",
    positivos,
    "Números negativos:",
    negativos,
)
