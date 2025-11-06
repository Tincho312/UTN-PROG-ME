def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)


num = int(input("Ingresá un número decimal: "))
print(f"Binario: {decimal_a_binario(num)}")
