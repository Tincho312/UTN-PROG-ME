import os


# Función: leer_alumnos
def leer_alumnos():
    alumnos = []
    diccionario = {}

    # Si no existe el archivo lo creamos vacío
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
    except (IOError, ValueError) as error_archivo:
        print(f"Error al leer el archivo: {error_archivo}")

    return alumnos, diccionario


# Función: mostrar_alumnos
def mostrar_alumnos(alumnos):
    if not alumnos:
        print("No hay alumnos cargados.")
    else:
        print("\n~ LISTA DE ALUMNOS ~")
        for alumno in alumnos:
            print(
                f"{alumno['nombre']} {alumno['apellido']} - Legajo: {alumno['legajo']} - Nota: {alumno['nota']}"
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
    except IOError as error_archivo:
        print(f"Error al guardar el alumno: {error_archivo}")


# Función: guardar_aprobados
def guardar_aprobados(alumnos):
    # Guarda en aprobados.txt a los alumnos con nota >= 6 y los muestra.
    aprobados = [alumno for alumno in alumnos if alumno["nota"] >= 6]

    try:
        with open("aprobados.txt", "w", encoding="utf-8") as archivo:
            for alumno_aprobado in aprobados:
                archivo.write(
                    f"{alumno_aprobado['nombre']};{alumno_aprobado['apellido']};{alumno_aprobado['legajo']};{alumno_aprobado['nota']}\n"
                )
    except IOError as error_archivo:
        print(f"Error al escribir en aprobados.txt: {error_archivo}")
        return

    print("\n~ APROBADOS ~")
    if not aprobados:
        print("No hay alumnos aprobados.")
    else:
        for alumno_aprobado in aprobados:
            print(
                f"{alumno_aprobado['nombre']} {alumno_aprobado['apellido']} - Legajo: {alumno_aprobado['legajo']} - Nota: {alumno_aprobado['nota']}"
            )
    print("-----------------\n")


# Menú principal
def menu():
    alumnos, diccionario = leer_alumnos()

    while True:
        print("|~~ MENÚ ~~|")
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
