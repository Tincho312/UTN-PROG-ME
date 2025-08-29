# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

# El usuario ingresa la edad
edad = int(input("Ingresa tu edad: "))
# Definimos a traves de condicionales multiples la categoria del usuario en base a la edad, 
# teniendo en cuenta los distintos rangos
# en caso de que la edad sea 0 o mayor a 105 el usuario debera introduccir logicamente la edad correcta.
if edad <= 12 and edad >= 1:
    print(f"Edad Ingresada: {edad}, Categoria: Niño")
elif edad >= 12 and edad <= 18:
    print(f"Edad Ingresada: {edad}, Categoria: Adolecente")
elif edad >= 12 and edad <= 30:
    print(f"Edad Ingresada: {edad}, Categoria: Adulto/a joven")    
elif edad >= 30 and edad <= 105:
    print(f"Edad Ingresada: {edad}, Categoria: Adulto/a mayor")
else:
    print("Ingrese correctamente la edad.")        
    