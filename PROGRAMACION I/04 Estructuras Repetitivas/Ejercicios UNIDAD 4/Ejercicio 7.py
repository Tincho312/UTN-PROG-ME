# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

numero_usuario = int(input("Ingrese un Número: "))

suma = 0
contador = 0
while contador <= numero_usuario:
    suma = suma + contador
    contador += 1

print("La suma de los digitos es: ", suma)
