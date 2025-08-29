# EJERCICIO 7 
# Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("Ingresa el primer numero (distinto de cero): "))
num2 = int(input("Ingresa el segundo numero (distinto de cero): "))

if num1 != 0 and num2 != 0:
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    
    print("\nResultados:")
    print("Suma:", suma)
    print("Resta:", resta)
    print("multiplicacion:", multiplicacion)
    print("division:", division)
    
else: 
    print("Error: los numeros deben ser distintos de 0.")