# Ejercicio 10: Eliminar un Elemento por su Índice
# Escribe un programa que permita al usuario ingresar una lista de números y eliminar
# un elemento en un índice especificado.
# Pedir al usuario la lista de números separados por comas
entrada = input("Ingresa números separados por comas: ")
numeros = [int(x) for x in entrada.split(",")]

# Pedir el índice a eliminar
indice = int(
    input(f"Ingresa el índice del elemento a eliminar (0 a {len(numeros)-1}): ")
)

# Validar que el índice sea correcto
if 0 <= indice < len(numeros):
    numeros.pop(indice)
    print("Lista actualizada:", numeros)
else:
    print("Índice inválido")
