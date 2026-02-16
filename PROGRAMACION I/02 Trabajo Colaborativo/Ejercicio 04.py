# 4- Desarrolle un programa que ayude a una cajera a determinar el número de billetes y
# monedas que se necesitan de cada una de las siguientes denominaciones 200, 100, 50,
# 20, 10, 5, 2 y 1, y monedas de 0.50, 0.25, 0.10 y 0.05 centavos para una cantidad de
# dinero dada. Ejemplo si la cantidad es 1390,55 se necesitan 6 billetes de 200, 1 billete
# de 100, 1 billete de 50, 2 billetes de 20, 1 moneda de 0.50 y una moneda de 0.05
# centavos. Plantee el algoritmo planteando métodos para su resolución.

dineroDado = float(input("Ingrese el total pagado"))

Total = dineroDado

# Billetes de 200
Billetes_200 = Total // 200
resto_billetes = Total % 200
print(f"Se necesitan {Billetes_200} billetes de 200")

# Billetes de 100
Billetes_100 = resto_billetes // 100
resto_billetes = resto_billetes % 100
print(f"Se necesitan {Billetes_100} billetes de 100")

# Billetes de 50
Billetes_50 = resto_billetes // 50
resto_billetes = resto_billetes % 50
print(f"Se necesitan {Billetes_50} billetes de 50")

# Billetes de 20
Billetes_20 = resto_billetes // 20
resto_billetes = resto_billetes % 20
print(f"Se necesitan {Billetes_20} billetes de 20")

# Billetes de 10
Billetes_10 = resto_billetes // 10
resto_billetes = resto_billetes % 10
print(f"Se necesitan {Billetes_10} billetes de 10")

# Billetes de 5
Billetes_5 = resto_billetes // 5
resto_billetes = resto_billetes % 5
print(f"Se necesitan {Billetes_5} billetes de 5")

# Billetes de 2
Billetes_2 = resto_billetes // 2
resto_billetes = resto_billetes % 2
print(f"Se necesitan {Billetes_2} billetes de 2")

# Billetes de 1
Billetes_1 = resto_billetes // 1
resto_billetes = resto_billetes % 1
print(f"Se necesitan {Billetes_1} billetes de 1")
# ------------------------------------------------------------------------------------#
total = resto_billetes
total = total * 100
# Monedas de 0.50
monedas_050 = total // 50
resto_monedas = total % 50
print(f"Se necesitan {monedas_050} monedas de 0.50")

# Monedas de 0.25
monedas_025 = resto_monedas // 25
resto_monedas = resto_monedas % 25
print(f"Se necesitan {monedas_025} monedas de 0.25")

# Monedas de 0.10
monedas_010 = resto_monedas // 10
resto_monedas = resto_monedas % 10
print(f"Se necesitan {monedas_010} monedas de 0.10")

print(f"Resto actual: {resto_monedas} ")

# Monedas de 0.05
monedas_005 = resto_monedas // 5 + 1
resto_monedas = resto_monedas % 5
print(f"Se necesitan {monedas_005} monedas de 0.05")
