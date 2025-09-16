# Ejercicio 9: Lista de Números Primos
# Escribe un programa que permita al usuario ingresar una lista de números y filtre los
# números primos.


# Función para determinar si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Pedir al usuario una lista de números separados por comas
entrada = input("Ingresa números separados por comas: ")
numeros = [int(x) for x in entrada.split(",")]

# Filtrar los números primos
primos = [num for num in numeros if es_primo(num)]

# Mostrar los números primos
print("Números primos:", primos)
