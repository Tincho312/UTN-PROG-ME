# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
# pantalla. 

texto = input("Escribe una frase o palabra: ")
# Verifico si termina en una vocal (mayúscula o minúscula)
if texto[-1] in "aeiouAEIOU":
# Añadir signo de exclamación si termina en vocal    
    texto += "!"
print(texto)
