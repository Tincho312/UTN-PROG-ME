# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numero_secreto = random.randint(0, 9)

intento_usuario = -1
intento = 0

while intento_usuario != numero_secreto:
    intento_usuario = int(input("Adivine el número aleatorio entre 0 y 9: "))
    intento += 1


print((f"¡Haz adivinado! - Juego finalizado en {intento} intentos"))
