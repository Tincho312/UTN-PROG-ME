# 2- Si se asigna un valor a una variable fuera de rango (mayor de lo establecido) ¿Qué
# ocurre? ¿Existe alguna forma de resolverlo? Ejemplifique.

# Respuesta: Si se asigna un valor fuera del rango ocurre un "desbordamiento" u "overflow" Ejemplo:

"""numeroGrande = 2**200000"""

# """---Esto daria error ya que el numero supera por mucho el limite---"""
"""print(f"Valor inicial= {numeroGrande}")"""

# Podemos usar un bucle para asignar un valor a una variable hasta que este dentro del limite establecido

contraseña_limite = 999
contra_usuario = 2000

while contra_usuario > contraseña_limite:
    contra_usuario = int(input("Ingrese su contraseña"))
    if contra_usuario < contraseña_limite:
        print("Contraseña correcta")
        break
