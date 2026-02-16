cadena = str(input("Ingrese una cadena de texto: "))
cont = 0

for i in range(0, len(cadena)):
    if (
        cadena[i].lower() == "a"
        or cadena[i] == "e"
        or cadena[i] == "i"
        or cadena[i] == "o"
        or cadena[i] == "u"
    ):
        cont += 1

print("El tamaño de la cadena es de:", len(cadena))
print("La cadena tiene", cont, "vocales")
