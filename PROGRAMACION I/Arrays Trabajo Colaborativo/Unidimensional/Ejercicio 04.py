# Escribe un programa que pida al usuario una lista de números y cuente cuántos de
# ellos son pares y cuántos son impares
# Inicializamos la lista y los contadores
numeros = []
pares = 0
impares = 0

print("Ingresa números uno por uno. Escribe 'fin' para terminar.")

while True:
    entrada = input("Ingresa un número: ")
    if entrada.lower() == "fin":
        break
    try:
        n = int(entrada)
        numeros.append(n)
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
    except ValueError:
        print("Eso no es un número válido. Intenta de nuevo.")

print("Números ingresados:", numeros)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
