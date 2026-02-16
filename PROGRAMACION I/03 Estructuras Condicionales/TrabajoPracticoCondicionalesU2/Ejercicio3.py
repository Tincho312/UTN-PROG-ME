# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

# El usuario ingresa un numero
numero = int(input("Ingresa un número: "))
# Si divide por 2 y el resto da 0 es numero par
if numero % 2 == 0:
    print(f"Ha ingresado un número par")
# caso contrario no es par y el usuario ingresa nuevamente el numero
else:
    print(f"Por favor, ingrese un número par")