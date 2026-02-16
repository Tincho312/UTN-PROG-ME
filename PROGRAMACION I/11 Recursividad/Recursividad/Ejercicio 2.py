def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


pos = int(input("Ingresá hasta qué posición mostrar la serie: "))
for i in range(pos):
    print(fibonacci(i))
