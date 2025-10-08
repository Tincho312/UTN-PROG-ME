import os


# Función: leer_alumnos
def leer_alumnos():
    alumnos = []
    diccionario = {}

    # Si no existe el archivo, crearlo vacío
    if not os.path.exists("alumnos.txt"):
        open("alumnos.txt", "w").close()
        return alumnos, diccionario

    try:
        with open("alumnos.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                nombre, apellido, legajo, nota = linea.split(";")
                nota = float(nota)
                alumno = {
                    "nombre": nombre,
                    "apellido": apellido,
                    "legajo": legajo,
                    "nota": nota,
                }
                alumnos.append(alumno)
                diccionario[legajo] = alumno
    except (IOError, ValueError) as e:
        print(f"Error al leer el archivo: {e}")

    return alumnos, diccionario


# Función: mostrar_alumnos
def mostrar_alumnos(alumnos):
    if not alumnos:
        print("No hay alumnos cargados.")
    else:
        print("\n~ LISTA DE ALUMNOS ~")
        for a in alumnos:
            print(
                f"{a['nombre']} {a['apellido']} - Legajo: {a['legajo']} - Nota: {a['nota']}"
            )
        print("------------------------\n")


# Función: validar_existe_alumno
def validar_existe_alumno(diccionario, legajo):
    # Devuelve True si el legajo ya existe en el diccionario.
    return legajo in diccionario


# Función: agregar_alumno
def agregar_alumno(alumnos, diccionario):
    # Agrega un nuevo alumno al archivo, validando datos y legajo repetido.
    print("\n~ AGREGAR NUEVO ALUMNO ~")

    while True:
        nombre = input("Nombre: ").strip()
        if nombre.isalpha():
            break
        print("Error: solo letras.")

    while True:
        apellido = input("Apellido: ").strip()
        if apellido.isalpha():
            break
        print("Error: solo letras.")

    while True:
        legajo = input("Legajo (5 dígitos): ").strip()
        if legajo.isdigit() and len(legajo) == 5:
            if validar_existe_alumno(diccionario, legajo):
                print(
                    f"El legajo {legajo} ya existe en alumnos.txt, no se permite su escritura.\n"
                )
                return
            break
        print("Error: debe tener 5 dígitos.")

    while True:
        try:
            nota = float(input("Nota promedio (1 a 10): ").strip())
            if 1 <= nota <= 10:
                break
            print("Error: debe ser entre 1 y 10.")
        except ValueError:
            print("Error: ingrese un número válido.")

    nuevo = {"nombre": nombre, "apellido": apellido, "legajo": legajo, "nota": nota}
    alumnos.append(nuevo)
    diccionario[legajo] = nuevo

    try:
        with open("alumnos.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre};{apellido};{legajo};{nota}\n")
        print("Alumno agregado correctamente.\n")
    except IOError as e:
        print(f"Error al guardar el alumno: {e}")


# Función: guardar_aprobados
def guardar_aprobados(alumnos):
    # Guarda en aprobados.txt a los alumnos con nota >= 6 y los muestra.
    aprobados = [a for a in alumnos if a["nota"] >= 6]

    try:
        with open("aprobados.txt", "w", encoding="utf-8") as archivo:
            for a in aprobados:
                archivo.write(
                    f"{a['nombre']};{a['apellido']};{a['legajo']};{a['nota']}\n"
                )
    except IOError as e:
        print(f"Error al escribir en aprobados.txt: {e}")
        return

    print("\n~ APROBADOS ~")
    if not aprobados:
        print("No hay alumnos aprobados.")
    else:
        for a in aprobados:
            print(
                f"{a['nombre']} {a['apellido']} - Legajo: {a['legajo']} - Nota: {a['nota']}"
            )
    print("-----------------\n")


# Menú principal
def menu():
    alumnos, diccionario = leer_alumnos()

    while True:
        print("===== MENÚ =====")
        print("1. Ver alumnos")
        print("2. Agregar alumno")
        print("3. Generar y mostrar aprobados")
        print("4. Salir")
        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            mostrar_alumnos(alumnos)
        elif opcion == "2":
            agregar_alumno(alumnos, diccionario)
        elif opcion == "3":
            guardar_aprobados(alumnos)
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida.\n")


# Ejecución del programa
if __name__ == "__main__":
    menu()
