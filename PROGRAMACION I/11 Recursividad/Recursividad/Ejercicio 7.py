def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)


niveles = int(input("Bloques en el nivel más bajo: "))
print(f"Total de bloques: {contar_bloques(niveles)}")
