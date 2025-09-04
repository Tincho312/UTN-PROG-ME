# 1CASTEO: Codifique un programa que solicite el ingreso de un número decimal y
# asigne el mismo a una variable valorDecimal, aplique las operaciones de CASTING para
# convertir la variable en otro tipo de dato. Investigue las diferentes formas de lograr la
# conversión. Muestre por pantalla el resultado de las conversiones

# De float a entero (trunca la parte decimal)
# num_float = 12.67
# num = int(num_float) # Resultado: 12"""

valorDecimal = float(input("Ingrese un numero decimal"))
valorEntero = int(valorDecimal)
print(f"Este es el valor del numero ingresado en entero {valorEntero}")

valorStr = str(valorDecimal)
print(f"Este es el valor del numero ingresado en str {valorStr}")

valorBool = bool(valorDecimal)
print(f"Este es el valor del numero ingresado en Booleano {valorBool}")

lista = list(valorStr)
print(f"Este es el valor ingresado en  una lista{lista}")

tupla = tuple(lista)
print(f"Este es el valor ingresado en una tupla{tupla}")

conjunto = set(lista)
print(f"Este es el valor ingresado en un conjunto{conjunto}")

listaTuplas = [(f"{valorEntero}", 1), (f"{valorDecimal}", 2), (f"{valorBool}", 3)]
diccionario = dict(listaTuplas)
print(f"Este es el valor ingresado en un diccionario{diccionario}")
