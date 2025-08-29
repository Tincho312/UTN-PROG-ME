# 2- Si se asigna un valor a una variable fuera de rango (mayor de lo establecido) ¿Qué 
# ocurre? ¿Existe alguna forma de resolverlo? Ejemplifique.  

numero = int(input("Ingrese un número entre 1 y 10: "))
if 1 <= numero <= 10:
    print("Número válido:", numero)
else:
    print("Error: número fuera de rango.")
