# escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

import statistics

import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calculamos estadísticas
media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
moda = statistics.mode(numeros_aleatorios)

# Imprimimos valores
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

# Determinamos el sesgo
if moda < media < mediana:
    print("Hay sesgo negativo (asimetría hacia la izquierda)")
elif moda > media > mediana:
    print("Hay sesgo positivo (asimetría hacia la derecha)")
else:
    print("No hay sesgo aparente (distribución simétrica)")
