# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

# El usuario ingresa una nota
nota = int(input("Ingresa tu nota: "))
# Si la nota es mayor o igual a 6 se imprime "aprobado"
if nota >= 6:
    print(f"Aprobado")
# caso contrario imprime "desaprobado"
else:
    print(f"Desaprobado")     