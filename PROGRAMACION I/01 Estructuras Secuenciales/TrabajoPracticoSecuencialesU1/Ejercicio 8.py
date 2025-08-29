# EJERCICIO 8
# Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo:
# 𝐼𝑀𝐶 =
# 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔
# (𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)
# 2

peso = float(input("Ingresa tu peso en Kg: "))
altura = float(input("Ingresa tu altura en Metros: "))
imc = peso / (altura ** 2)
print("\nTu Índice de Masa Corporal (IMC) es:", round(imc, 2))