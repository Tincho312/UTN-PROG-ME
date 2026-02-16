# Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.


def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")


# Pedir al usuario un número
numero_usuario = int(input("Introduce un número para ver su tabla de multiplicar: "))

# Llamar a la función
tabla_multiplicar(numero_usuario)
