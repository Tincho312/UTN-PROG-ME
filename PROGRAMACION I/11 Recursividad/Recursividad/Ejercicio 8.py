def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)


n = int(input("Número: "))
d = int(input("Dígito a contar: "))
print(f"El dígito {d} aparece {contar_digito(n, d)} veces.")
