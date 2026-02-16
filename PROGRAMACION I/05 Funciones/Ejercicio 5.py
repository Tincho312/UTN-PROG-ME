# Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.


# Función que convierte segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600


# Programa principal
if __name__ == "__main__":
    # Solicitar los segundos al usuario
    segundos = float(input("Ingresa la cantidad de segundos: "))

    # Calcular las horas
    horas = segundos_a_horas(segundos)

    # Mostrar el resultado
    print(f"{segundos} segundos equivalen a {horas:.2f} horas.")
