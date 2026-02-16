563  # 3- Codifique un algoritmo que solicite el ingreso de un numero de 3 dígitos (100 - 999)
# y por medio del uso de las operaciones matemáticas módulo 10 y división por 10
# efectué la suma de los 3 dígitos del número. Ejemplo ingreso 563, salida del algoritmo
# 14. Plantee el algoritmo planteando métodos para su resolución.

digitos = int(input("Ingrese un numero de 3 digitos para sumarlos"))

while digitos > 999 or digitos < 100:
    digitos = int(input("Ingrese un numero de 3 digitos por favor"))
    if digitos < 999 and digitos > 100:
        break

suma = 0
for i in range(3):
    ultimoDigito = digitos % 10
    suma = suma + ultimoDigito
    digitos = digitos // 10


print(f"La suma de los digitos es {suma}")
