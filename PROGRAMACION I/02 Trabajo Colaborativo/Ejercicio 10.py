cadena = str(input("Ingrese una cadena: "))
opc = 0

while opc != 1 or opc != 2:
    print("1 - Para convertir la cadena a mayusculas")
    print("2 - Para convertir la cadena a minusculas")
    opc = int(input("Ingrese una opcion: "))

    if opc == 1:
        print(cadena.upper())
        break
    elif opc == 2:
        print(cadena.lower())
        break
    else:
        print("Opcion no valida, intente de nuevo.")
