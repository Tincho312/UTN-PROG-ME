# Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    # Evitar división por cero
    if b != 0:
        division = a / b
    else:
        division = "Indefinido (división por cero)"

    return (suma, resta, multiplicacion, division)


a = 10
b = 5
suma, resta, multiplicacion, division = operaciones_basicas(a, b)

print(f"Operaciones con a = {a} y b = {b}:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
