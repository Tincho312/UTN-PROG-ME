# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
# dependiendo de la opción que desee: 
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# Pedimos el nombre al usuario
nombre = input("Ingresa tu nombre: ")

# Pedimos la opción deseada
print("Elige una opción:")
print("1 - Nombre en MAYÚSCULAS")
print("2 - Nombre en minúsculas")
print("3 - Nombre con la Primera Letra en mayúscula")
opcion = input("Ingresa 1, 2 o 3: ")

# Aplicamos la transformación según la opción
if opcion == '1':
    print(nombre.upper())
elif opcion == '2':
    print(nombre.lower())
elif opcion == '3':
    print(nombre.title())
else:
    print("Opción no válida.")
