# Crear una función llamada calcular_imc(peso, altura) que reciba el
#  peso en kilogramos y la altura en metros, y devuelva el índice de
#  masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
# ción para mostrar el resultado con dos decimales.


def calcular_imc(peso, altura):
    """Calcula el Índice de Masa Corporal (IMC)."""
    return peso / (altura**2)


# Solicitar datos al usuario
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

# Calcular IMC
imc = calcular_imc(peso, altura)

# Mostrar resultado con 2 decimales
print(f"Su IMC es: {imc:.2f}")
