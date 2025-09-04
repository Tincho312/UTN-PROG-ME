# Indique que sucede si realizo la siguiente declaracion de variable:
# x = None print(x)
# Explique y ejemplifique el uso de None

# Si se hace esa ejecución, x no hace nada, ya que la función None hace que la variable x no
# tenga un valor real o significativo por el momento, no las invalida pero las deja sin un valor.
# Ej: estoy haciendo un programa para una biblioteca que busca un libro por su título, si el libro
# se encuentra, devuelve un valor existente, pero si el libro no se encuentra bajo el catálogo,
# no devuelve un valor y devuelve None.
valor = input("Ingresa un valor: ")

if valor == "":
    valor = None

if valor is None:
    print("No se ha ingresado ningún valor.")
else:
    print(f"El valor ingresado es: {valor}")
