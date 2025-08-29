# 3- Codifique un algoritmo que solicite el ingreso de un numero de 3 dígitos (100 - 999) 
# y por medio del uso de las operaciones matemáticas módulo 10 y división por 10 
# efectué la suma de los 3 dígitos del número. Ejemplo ingreso 563, salida del algoritmo 
# 14. Plantee el algoritmo planteando métodos para su resolución. 

numero = int(input("Ingrese un numero de 3 digitos: "))
# validamos que tenga tres digitos
if 100 <= numero <= 999: 
    print("Numero valido de 3 digitos: ")
    print("sigamos...")
    #Recolectamos datos
    unidad = numero % 10
    decena = (numero // 10) % 10
    centena = numero // 100
    
    suma = unidad + decena + centena
    print("f: unidad:", {unidad}, "f: decena", {decena},"f: centena", {centena})
    print("Suma de los digitos", suma)
else:
    print("Numero ingresado invalido")
    


