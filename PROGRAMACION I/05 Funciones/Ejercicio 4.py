# Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

import math


# Función para calcular el área del círculo
def calcular_area_circulo(radio):
    return math.pi * radio**2


# Función para calcular el perímetro del círculo
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio


# Programa principal
if __name__ == "__main__":
    # Solicitar el radio al usuario
    radio = float(input("Ingresa el radio del círculo: "))

    # Calcular área y perímetro
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)

    # Mostrar los resultados
    print(f"El área del círculo es: {area:.2f}")
    print(f"El perímetro del círculo es: {perimetro:.2f}")
