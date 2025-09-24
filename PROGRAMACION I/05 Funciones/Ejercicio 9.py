#  Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#  una temperatura en grados Celsius y devuelva su equivalente en
#  Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#  resultado usando la función


def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit."""
    return (celsius * 9 / 5) + 32


# Pedir al usuario la temperatura en Celsius
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Llamar a la función y mostrar resultado
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius:.2f}°C equivalen a {fahrenheit:.2f}°F")
