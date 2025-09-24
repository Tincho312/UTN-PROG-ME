# Crear una función llamada calcular_promedio(a, b, c) que reciba
#  tres números como parámetros y devuelva el promedio de ellos.
#  Solicitar los números al usuario y mostrar el resultado usando esta
#  función.


def calcular_promedio(a, b, c):
    """Devuelve el promedio de tres números."""
    return (a + b + c) / 3


# Solicitar números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Calcular promedio
promedio = calcular_promedio(num1, num2, num3)

# Mostrar resultado
print(f"El promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")
