# Codifique un metodo que reciba como parametro una cadena y determine si la misma contiene o no numeros


def contiene_numeros(cadena):
    for caracter in cadena:
        if caracter.isdigit():
            return True
    return False


texto = input("Ingrese una cadena: ")
if contiene_numeros(texto):
    print("La cadena contiene numeros")
else:
    print("La cadena no contiene numeros")
