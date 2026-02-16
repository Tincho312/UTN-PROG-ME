# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

# Pedimos contraseña al usuario
contraseña = input("Ingrese una contraseña: ")
# comprobamos a traves de la funcion len(contraseña) si la longitud esta entre 8 y 14 caracteres
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña de longitud adecuada")
else: 
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
